from db.CRUD import UsersRepository
from datetime import date


crud_user = UsersRepository()
def format_data(data):
    try:

        return data.split('/')
    except:
        return False



while True:
    resposta = input('Type 1 to register a new user or 0 to leave: ')
    if not resposta.isnumeric():
        print('Wrong entered value')
        continue
    if resposta == '1':
        input_name = input('Enter a name: ')
        input_email = input('Enter an email: ')
        input_birthdate = input('Enter your birthdate: (dd/mm/yyyy) ')
        input_birthdate = formata_data(input_birthdate)
        if not len(input_birthdate) == 3:
            print('Incorrect date, please inform correctly!')
            continue
        input_birthdate = date(int(input_birthdate[2]), int(input_birthdate[1]), int(input_birthdate[0]))
        usuario_criado = crud_user.create(
            nome=input_name, email=input_email, aniversario=input_birthdate)
        if usuario_criado.id:
            print('User created successfully.')
    else:
        print('Leaving the program...')
        break
