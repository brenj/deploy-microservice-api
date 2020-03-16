pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'make install'
                sh 'pylint -d R0201,R0903 median/'
            }
        }
    }
}
