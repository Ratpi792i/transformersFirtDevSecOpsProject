pipeline {
    agent any

    triggers {
        githubPush()
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Ratpi792i/transformersFirtDevSecOpsProject.git'
            }
        }

        stage('SAST Semgrep') {
            steps {
                sh '''
                    /usr/local/bin/semgrep --config auto . \
                        --output rapport_semgrep.json --json || true
                '''
            }
        }

        stage('DAST ZAP') {
            steps {
                sh '''
                    sudo docker start dbe5bbc71ca4 || true
                    sleep 10
                    sudo docker run --rm \
                        ghcr.io/zaproxy/zaproxy:stable \
                        zap-baseline.py -t http://192.168.59.128:3000 \
                        -r zap_report.html || true
                '''
            }
        }

    }

    post {
        always {
            emailext(
                subject: "Pipeline DevSecOps - Build ${BUILD_NUMBER} - ${currentBuild.result}",
                body: """
                    Build : ${BUILD_NUMBER}
                    Statut : ${currentBuild.result}
                    Projet : transformers-devsecops
                    Lien : ${BUILD_URL}
                """,
                to: 'elieltena@gmail.com'
            )
        }
    }
}
