pipeline {
    agent any

    stages {
        stage('Clone repo') {
            steps {
                script{
                    if(fileExists('/home/jenkins/.jenkins/workspace/project1')){
                        sh 'cd Character-Randomiser && git pull'
                    }
                    else{
                        sh 'git clone https://github.com/Matambu/project1.git'
                    }
                }
            }
        }
        stage('Installs') {
            steps {
                sh 'pip3 install -r project/Service1/application/requirements.txt'
            }
        }
        stage(Testing) {
            steps {
                sh 'cd project1/Service1/ && python3 -m pytest --cov=application --cov-report term-missing'
                sh 'cd project1/Service2/ && python3 -m pytest --cov=application --cov-report term-missing'
                sh 'cd project1/Service3/ && python3 -m pytest --cov=application --cov-report term-missing'
                sh 'cd project1/Service4/ && python3 -m pytest --cov=application --cov-report term-missing'
            }
        }
        stage('Build and Push') {
            steps {
                sh 'cd project1 && docker compose build'
                sh 'cd project1 && docker compose push'
            }
        }
        stage('Deploy') {
            steps {
                sh 'cd project1 && docker compose up -d'
            }
        }
    }
}