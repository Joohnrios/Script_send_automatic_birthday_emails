from db.CRUD import UsersRepository
from datetime import date
from pprint import pprint

crud_user = UsersRepository()

usuario_criado = crud_user.create(nome='Fabricio', email='fabricio@hotmail.com', aniversario=date(1997, 8, 31))
print()
print('criacao', usuario_criado)
print('-'*150)

usuario = crud_user.read(id= usuario_criado.id)
print()
print('detalhe', usuario)
print('-'*150)


usuarios = crud_user.readAll()
print()
print('lista tudo')
pprint(usuarios)
print('-'*150)


print('usuario para ser alterado', usuarios[0])
usuario_alterar = crud_user.update(id= usuarios[0].id, name='Pedrada')

usuario = crud_user.read(id=usuarios[0].id)
print()
print('usuario alterado', usuario)
print('-'*150)

usuario_deletar = crud_user.delete(id=usuario.id)

