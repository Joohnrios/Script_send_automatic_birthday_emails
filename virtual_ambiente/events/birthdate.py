from db.CRUD import UsersRepository
from datetime import datetime
from emails.handler import enviar_email

def events_birthdate():
    crud_users = UsersRepository()

    aniversariantes = crud_users.get_birthdate(month=datetime.now().month, day=datetime.now().day)

    for aniversariante in aniversariantes:
        enviar_email(name=aniversariante.name, email_usuario=aniversariante.email)
        print('Email successfully sent!')
    print('All emails have been sent.')
