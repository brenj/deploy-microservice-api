create-eks-stack:
	aws cloudformation create-stack --stack-name median-microservice-eks --template-body file://aws/eks.yaml --parameters file://aws/eks-params.json

docker:
	docker build -t brenj/deploy-microservice-api:`cat VERSION` -f Dockerfile .

install:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt
	pip3 install -r test_requirements.txt

kubernetes-eks:
	aws eks update-kubeconfig --name median-microservice-prod

kubernetes-eks-deploy:
	sed "s/\%VERSION\%/`cat VERSION`/" aws/median-microservice.yaml
	kubectl apply -f aws/median-microservice.yaml
	kubectl apply -f aws/median-microservice-service.yaml

lint:
	docker run --rm -i hadolint/hadolint < Dockerfile
	python3 -m pylint -d R0201,R0903 --extension-pkg-whitelist=falcon median/

microservice:
	honcho start

test:
	pip3 install -r test_requirements.txt
	nosetests median/

update-eks-stack:
	aws cloudformation update-stack --stack-name median-microservice-eks --template-body file://aws/eks.yaml --parameters file://aws/eks-params.json

venv:
	python3 -m venv venv
