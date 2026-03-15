pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building project'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing project'
            }
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building project'
            }
        }

        stage('Run App') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing project'
            }
        }
    }
}

pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 jenkins-cicd-demo'
            }
        }

    }
}

pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 jenkins-cicd-demo'
            }
        }

    }
}

pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t jenkins-cicd-demo .'
            }
        }

        stage('Run Container') {
            steps {
                sh 'docker run -d -p 5000:5000 jenkins-cicd-demo'
            }
        }

    }
}
