pipeline {
    agent any
    triggers { githubPush() }
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Ratpi792i/transformersFirtDevSecOpsProject.git'
            }
        }
        stage('SAST Semgrep') {
            steps {
                sh '/usr/local/bin/semgrep --config auto . --output rapport_semgrep.json --json || true'
            }
        }
        stage('DAST ZAP') {
            steps {
                sh '''
                    pip3 install flask || true
                    python3 app.py &
                    sleep 10
                    mkdir -p /tmp/zap-reports
                    sudo docker run --rm \
                        --network host \
                        -v /tmp/zap-reports:/zap/wrk \
                        ghcr.io/zaproxy/zaproxy:stable \
                        zap-baseline.py \
                        -t http://127.0.0.1:5000 \
                        -r zap_report.html \
                        -I || true
                    ls -lh /tmp/zap-reports/
                    pkill -f "python3 app.py" || true
                '''
            }
        }
    }
    post {
        always {
            sh 'python3 /root/.jenkins/workspace/transformers-devsecops/send_email.py || true'
        }
    }
}
