install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	pylint median/

microservice:
	honcho start

test:
	pip install -r test_requirements.txt
	nosetests median/

venv:
	python3 -m venv venv
