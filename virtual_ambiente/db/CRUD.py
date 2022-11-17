from db.models import Pessoa
from db.models import session
from sqlalchemy import extract

class UsersRepository:

    def create(self, nome, email, aniversario): # Insert

        user1 = Pessoa(name=nome, email=email, birthdate=aniversario)
        
        session.add(user1)
        session.commit()
        return user1


    def read(self, id): # Select
        return session.query(Pessoa).filter(Pessoa.id == id).first() # Pode usar tbm o .first: ou o All
        
    
    def readAll(self):
      return session.query(Pessoa).all()
  

    def update(self, id, name=None, email=None, birthdate=None):
        data = dict()
        if name:
            data['name'] = name
        if email:
            data['email'] = email
        if birthdate:
            data['birthdate'] = birthdate

        session.query(Pessoa).filter(Pessoa.id == id).update(data)
        session.commit()
        return True
        


    def delete(self, id):
        session.query(Pessoa).filter(Pessoa.id == id).delete()
        session.commit()
        return True


    def get_birthdate(self, month, day):
        return session.query(Pessoa).filter(extract('month', Pessoa.birthdate)==month, extract('day', Pessoa.birthdate)==day).all()
