from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Date
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime



Base = declarative_base()
engine = create_engine('sqlite:///banco.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()  # Criando uma sessão (add, commit, query, etc). # Creating a session...



class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True) # autoincrement serve para o valor de um campo ser inserido automaticamente, toda vez q for criado.
    name = Column(String(40), index=True) # Index = Onde irá fazer mais buscas no banco. # Where you will do more bank searches.
    email = Column(String(20), nullable=False, unique=True) # Nullable = Não pode ficar vazio. # It cannot be empty.
    birthdate = Column(Date, nullable=False)
    created_id = Column(DateTime(), default=datetime.now)
    updated_id = Column(DateTime(), default=datetime.now, onupdate=datetime.now)


    def __repr__(self):  # Quando for printar um elemento, o método é chamado pra aparecer na tela mais legível. # When printing an element, the method is called to appear on the screen more readable.
        return f'Pessoa (id={self.id}, name={self.name}, email={self.email}, birthday={self.birthdate})'

    # Construtor = Utilizando o construtor para passar os valores no momento em que a classe é instanciada. :param name: (str)/ :param email: (str)/ :param birthday: (Date)
    def __init__(self, name, email, birthdate):

        self.name = name
        self.email = email
        self.birthdate = birthdate

Base.metadata.create_all(engine)  # Criando todas as tabelas. # Creating all tables.
