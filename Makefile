install:
	pip install --upgrade pip
	pip install -r requirements.txt

microservice:
	honcho start

test:
	pip install -r test_requirements.txt
	nosetests median/

venv:
	python3 -m venv venv
