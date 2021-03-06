__author__ = 'Jacek Kalbarczyk'

from os import path
from flask import Flask
from flask_bootstrap import Bootstrap
from config import DEBUG, HOST, PORT, DATABASE_URI
from views import stock_manager, login_manager
from views_products import stock_view
from models import db


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'DirtySecret'

Bootstrap(app)

app.register_blueprint(stock_manager)
app.register_blueprint(stock_view)


db.init_app(app)


login_manager.init_app(app)
login_manager.login_view = 'login'
app.static_path = path.join(path.abspath(__file__), 'static')


if __name__ == '__main__':
    app.run(HOST, PORT, debug=DEBUG)