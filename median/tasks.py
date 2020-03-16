"""Celery tasks."""

import os
import time

import celery
import numpy

from median.persistence import REDIS_APP

CELERY_APP = celery.Celery()
CELERY_APP.config_from_object('median.settings')


@CELERY_APP.task()
def get_median_for_last_min():
    """Get the median for the last minute from a specified time.

    Returns:
        int: The median for the last minute.
    """
    epoch_time = time.time()
    elements = REDIS_APP.zrangebyscore(
        os.environ['MEDIAN_SET_KEY'],
        epoch_time - float(os.environ['MEDIAN_LAST_X_SECONDS']), epoch_time)
    # elements e.g. ['7d529dd4-548b-4258-aa8e-23e34dc8d43d:200', ...]
    integers = [int(element.split(b':')[1]) for element in elements]

    # Don't give numpy an empty list
    return numpy.median(integers or 0)


@CELERY_APP.task()
def remove_old_integers():
    """Remove integers that will not be included in median calculation."""
    epoch_time = time.time()
    removed = REDIS_APP.zremrangebyscore(
        'integers', '-inf',
        epoch_time - float(os.environ['REMOVE_LAST_X_SECONDS']))
    print("{0} old elements removed from {1} set.".format(
        removed, os.environ['MEDIAN_SET_KEY']))
