"""
Nomes dos servidores SMTP para cada infraestrutura de email:
Gmail - smtp.gmail.com
Outlook.com/Hotmail.com - smtp-mail.outlook.com
Yahoo Mail - smtp.mail.yahoo.com

Porta:587
"""

import smtplib
import ssl
import email.message

msg = email.message.Message()

msg["Subject"] = "Assunto no Cabeçalho"

body = """ <h1>Titulo do Email<h1> <p>Assunto do email<p>"""

msg["From"] = "Mensageiro"
password = "*********"

msg["To"] = "Destinatario"

msg.add_header("Content-Type", "text-html")
msg.set_payload(body)

contexto = ssl.create_default_context()

with smtplib.SMTP("smtp.gmail.com", 587) as conexao:
    conexao.ehlo()
    conexao.starttls(context=contexto)
    conexao.login(msg["From"], msg["To"])
    conexao.sendmail(msg["From"], msg["To"], msg.as_string().encode("utf-8"))
