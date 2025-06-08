import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

email = "email.com"
senha = "senha de app"  

def envia(login, notificacao):
    msg = MIMEMultipart()
    msg["From"] = email
    msg["To"] = login
    msg["Subject"] = "Diario Oficial"
    msg.attach(MIMEText(notificacao, "plain"))

    # Enviar
    servidor = smtplib.SMTP("smtp.gmail.com", 587)
    servidor.starttls()
    servidor.login(email, senha)
    servidor.send_message(msg)
    servidor.quit()
    print("ENVIADO!")




