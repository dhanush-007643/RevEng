pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking Source Code'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t student-app .'
            }
        }

        stage('Run Container') {
            steps {
                bat 'docker run -d -p 5000:5000 --name student-container student-app || exit 0'
            }
        }
    }
}