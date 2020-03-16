pipeline {
    agent any
    stages {
        stage('Lint') {
            steps {
                sh 'make venv && source venv/bin/activate'
                sh 'make install'
                sh 'python3 -m pylint -d R0201,R0903 --extension-pkg-whitelist=falcon median/'
            }
        }
    }
}
