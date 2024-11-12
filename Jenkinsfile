pipeline {
    agent any

    stages {

        stage('Ajustar permisos') {
            steps {
                sh 'chmod -R u+w USQL pedidos trivia'
            }
        }

        stage('Correr Trivia - Python') {
            steps {
                sh 'source hola/bin/activate'
                dir('trivia') {
                    sh 'python3 -m pip install -r requirements.txt'
                    echo 'Building trivia...'
                    sh 'python3 -m pydoc -w trivia'
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
                    sh 'python3 -m pydoc -w main'
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
                    sh 'javadoc -d docs Main.java'
                    sh 'ls -l'
                }
            }
        }

        stage('Archive') {
            steps {
                // Archivar el archivo trivia.html como artefacto
                archiveArtifacts allowEmptyArchive: true, artifacts: 'trivia/trivia.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'USQL/main.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'pedidos/docs/Main.html'
                archiveArtifacts allowEmptyArchive: true, artifacts: 'pedidos/docs/*'
            }
        }

        stage('Test') {
            steps {
                echo 'Testing...'
                dir('USQL') {
                    sh 'python3 -m pytest test_proyect.py'
                }
            }
        }
        
    }
}