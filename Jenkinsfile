pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'pylint median/'
            }
        }
    }
}
