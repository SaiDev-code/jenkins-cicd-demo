pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image'
                sh 'docker build -t jenkins-cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running Docker container'
                sh 'docker run -d -p 5000:5000 jenkins-cicd-demo'
            }
        }

    }
}



