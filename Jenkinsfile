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
    }
}
