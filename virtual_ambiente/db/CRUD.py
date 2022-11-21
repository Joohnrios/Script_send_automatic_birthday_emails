from db.models import User
from db.models import session
from sqlalchemy import extract

class UsersRepository:

    def create(self, nome, email, aniversario): # Insert

        user1 = User(name=nome, email=email, birthdate=aniversario)
        
        session.add(user1)
        session.commit()
        return user1


    def read(self, id): # Select
        return session.query(User).filter(User.id == id).first() # Pode usar tbm o .first: ou o All
        
    
    def readAll(self):
      return session.query(User).all()
  

    def update(self, id, name=None, email=None, birthdate=None):
        data = dict()
        if name:
            data['name'] = name
        if email:
            data['email'] = email
        if birthdate:
            data['birthdate'] = birthdate

        session.query(User).filter(User.id == id).update(data)
        session.commit()
        return True
        


    def delete(self, id):
        session.query(User).filter(User.id == id).delete()
        session.commit()
        return True


    def get_birthdate(self, month, day):
        return session.query(User).filter(extract('month', User.birthdate)==month, extract('day', User.birthdate)==day).all()
