import sqlalchemy
from sqlalchemy.orm import sessionmaker
from models1 import create_tables,publisher, shop, book, stok, sale

def connection():
    print("Введите: ")
    driver = input("Драйвер подключения - ")
    login = input("Логин - ")
    password = input("Пароль - ")
    name_connection = input("Название подключения - ")
    port = input("Порт - ")
    name_db = input("Имя б.д. - ")
    return f"{driver}://{login}:{password}@{name_connection}:{port}/{name_db}"

def search(session):
    print("Выберите способ поиска: ")
    print("1)Id")
    print("2)Name")
    com = int(input())
    if com == 1:
        id = int(input("Введите id: "))
        print(session.query(publisher).filter(id == id).all()[0])
    elif com == 2:
        name = input("Введите имя: ")
        print(session.query(publisher).filter(name == name).all()[0])
    else:
        print("Команда не распознанна")

DSN = connection()
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

search(session)

session.close()