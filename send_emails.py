import smtplib
import ssl
import email.message
import os

# Configuração dos servidores SMTP para diferentes provedores de e-mail
servidores_smtp = {
    'Gmail': 'smtp.gmail.com',
    'Outlook': 'smtp-mail.outlook.com',
    'Yahoo': 'smtp.mail.yahoo.com'
}

# Escolha do servidor
servidor_escolhido = servidores_smtp['Gmail']
smtp_server = servidores_smtp[servidor_escolhido]
porta = 587  # Porta padrão para TLS

# Criação da mensagem
msg = email.message.EmailMessage()
msg["Subject"] = "Assunto do E-mail"
msg["From"] = "Email do Remetente"
msg["To"] = "Email do Destinatário"
password = 'Sua senha'  # Idealmente, usar variável de ambiente

# HTML do corpo do e-mail
body = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Seu Email Especial</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }
        .container {
            background-color: #ffffff;
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .header {
            background-color: #007BFF;
            color: #ffffff;
            padding: 10px;
            text-align: center;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
        .footer {
            padding: 10px;
            text-align: center;
            font-size: 12px;
            color: #777;
        }
        .button {
            display: inline-block;
            padding: 10px 20px;
            margin: 10px 0;
            background-color: #28a745;
            color: white;
            text-decoration: none;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Bem-Vindo(a) ao Nosso Newsletter!</h1>
        </div>
        <div class="content">
            <p>Este é um exemplo de e-mail HTML. Clique no botão abaixo para uma interação simples (Nota: o JavaScript pode não funcionar no seu cliente de e-mail).</p>
            <a href="https://ava3.uniube.br/login/" class="button">Clique Aqui!</a>
        </div>
        <div class="footer">
            <p>Você recebeu este e-mail porque se inscreveu em nosso serviço. Se deseja cancelar a subscrição, clique aqui.</p>
        </div>
    </div>
</body>
</html>
"""

msg.set_content(body, subtype='html')  # Define o tipo de conteúdo como HTML

# Criação do contexto SSL
contexto = ssl.create_default_context()

# Conexão com o servidor SMTP
try:
    with smtplib.SMTP(smtp_server, porta) as conexao:
        conexao.ehlo()  # Envio de uma saudação para o servidor
        conexao.starttls(context=contexto)  # Início da criptografia TLS
        conexao.login(msg["From"], password)  # Login usando o email do remetente e senha
        conexao.send_message(msg)  # Envio da mensagem
        print("Email enviado com sucesso!")
except Exception as e:
    print(f"Erro ao enviar email: {e}")
