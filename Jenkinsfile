pipeline {
    agent any

    // Cenário 4: build agendado a cada minuto (apenas para a demonstração)
    triggers {
        cron('* * * * *')
    }

    stages {
        stage('Preparar ambiente') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        // Cenário 2: erro de sintaxe no fonte faz esta etapa falhar (build FAILURE)
        stage('Build (compilar)') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m compileall -q src
                '''
            }
        }

        // Cenário 3: testes falhando deixam o build UNSTABLE (o '|| true' evita FAILURE,
        // e o junit marca o build como instável ao ler as falhas)
        stage('Testes') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest --junitxml=resultados.xml || true
                '''
            }
            post {
                always {
                    junit 'resultados.xml'
                }
            }
        }

        // Cenário 5 (bônus): cobertura de código
        stage('Cobertura') {
            steps {
                sh '''
                    . .venv/bin/activate
                    python -m pytest --cov=src --cov-report=term-missing --cov-report=xml:coverage.xml || true
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'coverage.xml', allowEmptyArchive: true
                }
            }
        }
    }
}
