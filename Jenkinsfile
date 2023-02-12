pipeline {
    agent any
    stages {
        stage('check the files') {
            steps {
                sh 'pwd'
                sh 'ls -la'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker-compose up -d --build'
            }
        }
        stage('clear cache') {
            steps {
                sh 'docker builder prune -af'
            }
        }
    }
    post {
        always {
            echo 'Cleanup after everything!'
        }
    }
}