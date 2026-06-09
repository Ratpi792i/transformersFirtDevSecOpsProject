import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

smtp_server = "smtp.gmail.com"
port = 587
sender = "elieltena@gmail.com"
password = "knhdbxbxouddhvqg"
receiver = "elieltena@gmail.com"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Jenkins DevSecOps - Rapport ZAP + Semgrep"

body = """
Pipeline DevSecOps - Rapport de Build

Projet  : transformersFirtDevSecOpsProject
SAST    : Semgrep - 435 findings detectes
DAST    : ZAP Baseline Scan - 7 warnings detectes
         - Missing Anti-clickjacking Header
         - X-Content-Type-Options Header Missing
         - Server Leaks Version Information
         - Content Security Policy Not Set
         - Permissions Policy Header Not Set
         - Cross-Origin-Embedder-Policy Missing

Rapport ZAP complet en piece jointe.
"""

msg.attach(MIMEText(body, "plain"))

# Attache le rapport ZAP
zap_report = "/tmp/zap-reports/zap_report.html"
if os.path.exists(zap_report):
    with open(zap_report, "rb") as f:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(f.read())
        encoders.encode_base64(part)
        part.add_header("Content-Disposition", "attachment; filename=zap_report.html")
        msg.attach(part)
    print("Rapport ZAP joint a l email !")
else:
    print("Rapport ZAP non trouve !")

server = smtplib.SMTP(smtp_server, port)
server.ehlo()
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()
print("Email envoye avec succes !")
