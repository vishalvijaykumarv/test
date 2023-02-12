pipeline {
    agent any
    stages {
        stage('build') {
            steps {
                sh 'docker-compose build --no-cache'
            }
        }
        stage('deploy') {
            steps {
                sh 'docker-compose up -d --force-recreate'
            }
        }
        stage('Release to prod') {
            steps {
                sh 'docker ps'
                sh 'echo Releasing to prod'
            }
        }
    }
    post {
        always {
            echo 'Cleanup after everything!'
            sh 'docker system prune --all -y'
        }
    }
}