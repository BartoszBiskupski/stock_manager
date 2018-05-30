__author__ = 'Jacek Kalbarczyk'

from main import app, db
from models import User, Product
from werkzeug.security import generate_password_hash
from sqlalchemy.orm.mapper import configure_mappers
import sqlalchemy as sa


admin = User(
    active=True,
    username="admin",
    password=generate_password_hash('admin', method='sha256'),
    email='admin@gmail.com',
    admin=True,
    # poweruser=True,
)


# dodanie przykładowych produktów i klientów
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

sa.orm.configure_mappers()
app.app_context().push()

db.create_all()
db.session.add(product1)
db.session.add(product2)
db.session.add(product3)
db.session.add(admin)


db.session.commit()

print('DB set up successfully!')
