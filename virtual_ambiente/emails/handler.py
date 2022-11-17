import smtplib
import email.message


# Função para enviar o email...
def enviar_email(name, email_usuario):
    corpo_email = f"""
    <p> Salve meu/minha little bro!</p>
    <p> Feliz aniversário {name}, tudo de bom e de melhor para você e sua familia, você é barril ao ²! ;)</p>
    <p> É NOIX! <3</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Parabéns!!!"
    msg['From'] = 'joohnsrios@gmail.com'
    msg['To'] = email_usuario
    password = 'fcvzswbtezdhhstj'  # senha do from = remetente
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login com as credenciais para enviar o email.
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Enviado com sucesso!')

