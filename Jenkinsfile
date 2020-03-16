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
                sh 'make lint'
            }
        }
        stage('Dockerize') {
            steps {
                sh 'make docker'
            }
        }
        stage('Publish') {
            steps {
                withDockerRegistry([credentialsId: "docker-hub", url: ""]) {
                    sh 'docker push brenj/deploy-microservice-api'
                }
            }
        }
    }
}
