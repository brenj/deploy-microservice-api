pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'python3 -m pylint median/'
            }
        }
    }
}
