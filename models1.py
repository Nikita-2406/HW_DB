import sqlalchemy as sq
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class publisher(Base):
    __tablename__ = 'publisher'

    id = sq.Column(sq.INTEGER, primary_key=True)
    name = sq.Column(sq.String(length=40))

    def __str__(self):
        return f'ID - {self.id} \nName - {self.name}'


class shop(Base):
    __tablename__ = 'shop'

    id = sq.Column(sq.INTEGER, primary_key=True)
    name = sq.Column(sq.String(length=40))


class book(Base):
    __tablename__ = 'book'

    id = sq.Column(sq.INTEGER, primary_key=True)
    title = sq.Column(sq.String(length=40))
    id_publisher = sq.Column(sq.INTEGER, sq.ForeignKey('publisher.id'))


class stok(Base):
    __tablename__ = 'stok'

    id = sq.Column(sq.INTEGER, primary_key=True)
    id_book = sq.Column(sq.INTEGER, sq.ForeignKey('book.id'))
    id_shop = sq.Column(sq.INTEGER, sq.ForeignKey('shop.id'))
    count = sq.Column(sq.INTEGER)


class sale(Base):
    __tablename__ = 'sale'

    id = sq.Column(sq.INTEGER, primary_key=True)
    prise = sq.Column(sq.INTEGER)
    date_sale = sq.Column(sq.DATE)
    id_stock = sq.Column(sq.INTEGER, sq.ForeignKey('stok.id'))
    count = sq.Column(sq.INTEGER)


def create_tables(engine):
    #Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
