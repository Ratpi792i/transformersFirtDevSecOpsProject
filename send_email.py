import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587
sender = "elieltena@gmail.com"
password = "knhdbxbxouddhvqg"
receiver = "elieltena@gmail.com"

msg = MIMEMultipart()
msg["From"] = sender
msg["To"] = receiver
msg["Subject"] = "Jenkins DevSecOps - Build Termine"

body = "Pipeline DevSecOps - Semgrep 435 findings - ZAP Baseline Scan - Build termine"
msg.attach(MIMEText(body, "plain"))

server = smtplib.SMTP(smtp_server, port)
server.ehlo()
server.starttls()
server.login(sender, password)
server.sendmail(sender, receiver, msg.as_string())
server.quit()
print("Email envoye!")
