__author__ = 'Jacek Kalbarczyk'

#from flask_login import UserMixin
from sqlalchemy_utils.types import TSVectorType
#from sqlalchemy import Column
#from sqlalchemy.types import Integer
#from sqlalchemy.types import String
#from sqlalchemy.types import Boolean

from flask_sqlalchemy import SQLAlchemy, BaseQuery
from sqlalchemy_searchable import make_searchable, SearchQueryMixin

db = SQLAlchemy()

make_searchable()

class ProductQuery(BaseQuery, SearchQueryMixin):
    pass


class User(db.Model):
    """
    User model for reviewers.
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    active = db.Column(db.Boolean, default=True)
    username = db.Column(db.String(200), unique=True)
    email = db.Column(db.String(200), default='')
    password = db.Column(db.String(200), default='')
    admin = db.Column(db.Boolean, default=False)

    def is_active(self):
        """
        Returns if user is active.
        """
        return self.active

    def is_admin(self):
        """
        Returns if user is admin.
        """
        return self.admin

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

class Product(db.Model):
    """
    Products in our app
    """
    # __tablename__ = 'products'
    # product_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    # product_name = db.Column(db.String(100))
    # product_catalog = db.Column(db.String(100))
    # product_description = db.Column(db.String(500))
    # product_price = db.Column(db.String(100))

    __tablename__ = 'products'
    __searchable__ = ['id', 'name', 'group']
    query_class = ProductQuery
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    group = db.Column(db.String(30), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    price = db.Column(db.Integer, default=0)
    search_vector = db.Column(TSVectorType('name', 'group',))

    # def __repr__(self):
    #     return "Products(id={}, name='{}', group='{}', quantity='{}', price='{}'".format(self.id, self.name, self.group,
    #                                                                                      self.quantity, self.price)
