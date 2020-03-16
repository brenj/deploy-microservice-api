"""A Median Microservice API."""

import json
import os
import time
import uuid

import falcon

from median.persistence import REDIS_APP
from median.tasks import CELERY_APP, get_median_for_last_min


class IntegerResource():
    """Resource for managing the integers used to calculate a median."""

    def on_post(self, req, resp):
        """Handle any integer."""
        integer = req.get_param_as_int('integer', required=True)

        # Set elements must be unique
        id_ = uuid.uuid4()
        element_name = ':'.join(map(str, (id_, integer)))

        elements_added = REDIS_APP.zadd(
            os.environ['MEDIAN_SET_KEY'], {element_name: time.time()})
        added_successfully = elements_added == 1

        resp.status = (
            falcon.HTTP_201 if added_successfully else falcon.HTTP_500)


class MedianResource():
    """Resource for managing the calculation of a median."""

    def on_get(self, req, resp):
        """Handle requests for the median in the last minute."""
        del req # unused

        task = get_median_for_last_min.delay()

        result_url = os.path.join(
            os.environ['MEDIAN_API_URL'], 'result', task.id)
        resp.body = json.dumps({'result_url': result_url})
        resp.status = falcon.HTTP_200


class ResultResource():
    """Resource for retrieving a median result."""

    def on_get(self, req, resp, task_id):
        """Handle requests for a median result."""
        del req # unused

        task = CELERY_APP.AsyncResult(task_id)

        resp.body = json.dumps(
            {'status': task.status, 'result': str(task.result)})
        resp.status = falcon.HTTP_200


APP = falcon.API()
APP.req_options.auto_parse_form_urlencoded = True

APP.add_route('/put', IntegerResource())
APP.add_route('/median', MedianResource())
APP.add_route('/result/{task_id}', ResultResource())
