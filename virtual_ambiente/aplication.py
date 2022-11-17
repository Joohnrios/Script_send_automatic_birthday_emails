from db.CRUD import UsersRepository
from datetime import date


crud_user = UsersRepository()
def formata_data(data):
    try:

        return data.split('/')
    except:
        return False



while True:
    resposta = input('Digite 1 para cadastrar um novo usuário ou 0 para sair: ')
    if not resposta.isnumeric():
        print('Valor digitado incorreto')
        continue
    if resposta == '1':
        input_name = input('Digite um nome: ')
        input_email = input('Digite um email: ')
        input_birthdate = input('Digite sua data de nascimento Ex: dd/mm/aaaa ')
        input_birthdate = formata_data(input_birthdate)
        if not len(input_birthdate) == 3:
            print('Data incorreta, por favor informe do jeito certo!')
            continue
        input_birthdate = date(int(input_birthdate[2]), int(input_birthdate[1]), int(input_birthdate[0]))
        usuario_criado = crud_user.create(
            nome=input_name, email=input_email, aniversario=input_birthdate)
        if usuario_criado.id:
            print('Usuário criado com sucesso.')
    else:
        print('Saindo do programa...')
        break