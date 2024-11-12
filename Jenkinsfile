pipeline {
    agent any

    stages {
        stage('Correr trivia python') {
            steps {
                sh 'source hola/bin/activate'
                dir('trivia') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building trivia...'
                    sh 'python3 -m pydoc -w trivia.py'
                }    
            }
        }

         stage('Correr USQL python') {
            steps {
                sh 'source hola/bin/activate'
                dir('USQL') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building USQL...'
                    sh 'python3 -m pydoc -w main.py'
                }    
            }
        }

        stage('Correr pedidos java') {
            steps {
                echo 'Building...'
                dir('pedidos') {
                    sh 'javac Main.java'
                    sh 'java Main'
                    
                }
            }
        }
        
        stage('Test') {
            steps {
                echo 'Testing...'
                // Insert your test commands here, e.g., sh 'make test' or sh 'npm test'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Deploying...'
                // Insert your deploy commands here, e.g., sh 'make deploy'
            }
        }
    }
}