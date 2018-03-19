__author__ = 'Jacek Kalbarczyk'

from sqlalchemy import create_engine
from main import db
from models import User, Product
from werkzeug.security import generate_password_hash

def db_start():
    create_engine('sqlite:///test.db', convert_unicode=True)
    db.create_all()
    db.session.commit()

    user = User()
    user.username = "admin"
    user.password = generate_password_hash('admin', method='sha256')
    user.email = 'admin@gmail.com'
    user.admin = True
    user.poweruser = True
    db.session.add(user)

#dodanie przykładowych produktów i klientów
product1 = Product(
    name='Car tire A',
    group='Tires',
    quantity=1,
    price=50
)
product2 = Product(
    name='Car tire B',
    group='Tires',
    quantity=3,
    price=60
)
product3 = Product(
    name='Car piston A',
    group='Pistons',
    quantity=1,
    price=150
)

products = Product.query.order_by(Product.id)
for product in products:
    print(product.id, product.name)
if __name__ == '__main__':
    db_start()
