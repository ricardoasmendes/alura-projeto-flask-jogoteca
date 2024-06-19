from dotenv import load_dotenv
import os

load_dotenv()

database_host = os.getenv('HOST')
database_username = os.getenv('USER')
database_password = os.getenv('PASSWORD')


SECRET_KEY = 'alura'

SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = database_username,
        senha = database_password,
        servidor = database_host,
        database = 'jogoteca'
    )