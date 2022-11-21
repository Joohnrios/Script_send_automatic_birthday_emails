import smtplib
import email.message


# Função para enviar o email...
def send_email(name, email_user):
    corpo_email = f"""
    <p> Hello my little bro!</p>
    <p> Congratulations {name}, all the best to you and your family...</p>
    <p> <3 <3 </p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Congratulations!!!"
    msg['From'] = 'your_email@...'
    msg['To'] = email_usuer
    password = 'fcvzswbtezdhhstj'  # senha do from = remetente # from password
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login com as credenciais para enviar o email. # Login with the credentials to send the email.
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Sent with success!')

