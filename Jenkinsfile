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
                    sleep 15
                    mkdir -p /tmp/zap-reports
                    sudo docker run --rm \
                        --network host \
                        -v /tmp/zap-reports:/zap/wrk \
                        ghcr.io/zaproxy/zaproxy:stable \
                        zap-baseline.py \
                        -t http://127.0.0.1:3000 \
                        -r zap_report.html \
                        -I || true
                    ls -lh /tmp/zap-reports/
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
