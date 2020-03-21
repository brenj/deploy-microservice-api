Project: Capstone
=================

About
-----
From Udacity:
> In the capstone project, each project is unique to the student. You’ll
build a CI/CD pipeline for a microservices application for different deployment
strategies. Students define the scope of the project and select the right
deployment strategy based on different business requirements.

The project code I chose to build my CI/CD pipeline around is a median
microservice. It is a REST api that allows the submission of integer values
and the asynchronous retrieval of a median for the set of submitted integers
over a certain interval (one minute by default). Among other technologies, it
leverages Redis and RabbitMQ.

Requirements
------------
* AWS Account
* awscli

Configuration
-------------
All app configuration is accomplished by environmental variables. See [.env](.env)

Deploy
------
1. `create-eks-stack`
2. `make kubernetes-eks`
3. `make kubernetes-eks-deploy` 

Usage Example
-------------
```console
brenj$ http --form POST a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/put integer=2
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2020 23:51:30 GMT
Server: gunicorn/20.0.4
content-length: 0

brenj$ http --form POST a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/put integer=3
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2020 23:51:33 GMT
Server: gunicorn/20.0.4
content-length: 0

brenj$ http --form POST a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/put integer=1
HTTP/1.1 201 Created
Connection: close
Date: Sun, 13 Mar 2020 23:51:36 GMT
Server: gunicorn/20.0.4
content-length: 0

brenj$ http GET a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/median
HTTP/1.1 200 OK
Connection: close
Date: Sun, 13 Mar 2020 23:51:43 GMT
Server: gunicorn/20.0.4
content-length: 65
content-type: application/json; charset=utf-8

{
    "result_url": "a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/result/b303f13d-d716-4224-86c7-478b14d0ca77" 
}

brenj$ http GET a683ac84585ce49b292abc1243161670-1888357290.us-west-2.elb.amazonaws.com:8000/result/b303f13d-d716-4224-86c7-478b14d0ca77
HTTP/1.1 200 OK
Connection: close
Date: Sun, 13 Mar 2020 23:51:57 GMT
Server: gunicorn/20.0.4
content-length: 38
content-type: application/json; charset=utf-8

{
    "result": "2.0", 
    "status": "SUCCESS"
}
```

Screenshots
-----------

Full Jenkins Pipeline
![Full Jenkins Pipeline](screenshots/full_jenkins_pipeline.png?raw=true)

Before Rolling Deployment
![Before Rolling Deployment](screenshots/before_rolling_deployment.png?raw=true)

After Rolling Deployment
![After Rolling Deployment](screenshots/after_rolling_deployment.png?raw=true)

Grading (by Udacity)
--------------------
Criteria                              |Highest Grade Possible  |Grade Recieved
--------------------------------------|------------------------|--------------------
Set Up Pipeline                       |Meets Specifications    |
Build Docker Container                |Meets Specifications    |
Successful Deployment                 |Meets Specifications    |
