__author__ = 'Jacek Kalbarczyk'

from os import path
from flask import Flask
from flask_bootstrap import Bootstrap
from config import DEBUG, HOST, PORT, DATABASE_URI
from views import stock_manager, login_manager
from views_products import stock_view
from models import db, Product
import flask_whooshalchemy as wh



DATABASE_URI = 'postgresql://{user}:{pw}@{url}/{db}'.format(user='postgres',pw='JW88qk28as95',url=HOST,db='stock_manager')


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'DirtySecret'
app.config['WHOOSH_BASE'] = 'whoosh'

Bootstrap(app)

wh.whoosh_index(app, Product)
app.register_blueprint(stock_manager)
app.register_blueprint(stock_view)


db.init_app(app)


login_manager.init_app(app)
login_manager.login_view = 'login'
app.static_path = path.join(path.abspath(__file__), 'static')


if __name__ == '__main__':
    app.run(HOST, PORT, debug=DEBUG)