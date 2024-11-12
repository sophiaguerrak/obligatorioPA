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

        post {
            always {
                // Archivar los archivos HTML generados
                archiveArtifacts artifacts: '**/docs/*.html', allowEmptyArchive: true
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying...'
                sh 'python3 -m http.server 8000 &'
                sleep 5
            }
        }
    }
}