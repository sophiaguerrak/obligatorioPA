pipeline {
    agent any

    stages {
        stage('hola') {
            steps {
                sh 'ls -ld trivia USQL pedidos'
            }
        }

        stage('Correr Trivia - Python') {
            steps {
                sh 'source hola/bin/activate'
                dir('trivia') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building trivia...'
                    sh 'python3 -m pydoc -w trivia.py'
                    sh 'ls -l'
                }    
            }
        }

         stage('Correr USQL - Python') {
            steps {
                sh 'source hola/bin/activate'
                dir('USQL') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building USQL...'
                    sh 'python3 -m pydoc -w main.py'
                    sh 'ls -l'
                }    
            }
        }

        stage('Correr Pedidos - Java') {
            steps {
                echo 'Building...'
                dir('pedidos') {
                    sh 'javac EmpaquetadoTask.java EnvioTask.java PagoTask.java Pedido.java ProcesadorPedidos.java'
                    sh 'javac Main.java'
                    sh 'java Main'
                    sh 'ls -l'
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