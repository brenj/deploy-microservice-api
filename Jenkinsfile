pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'make install'
            }
        }
        stage('Lint') {
            steps {
                sh 'python3 -m pylint -d R0201,R0903 --extension-pkg-whitelist=falcon median/'
            }
        }
        stage('Dockerize') {
            steps {
                sh 'make docker'
            }
        }
        stage('Publish') {
            steps {
                withDockerRegistry([credentialsId: "docker-hub", url: "https://hub.docker.com/repository/docker/brenj/deploy-microservice-api"]) {
                    sh 'docker push brenj/deploy-microservice-api'
                }
            }
        }
    }
}
