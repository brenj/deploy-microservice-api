pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'pylint -d R0201,R0903 median/'
            }
        }
    }
}
