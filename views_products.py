from sqlite3 import IntegrityError

from flask import render_template, redirect, url_for, request, Blueprint
# from flask_login import login_user, login_required, logout_user, current_user
# from main import login_manager
# from forms import LoginForm, SignupForm
from models import Product, db
# from sqlalchemy.exc import IntegrityError
# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import asc
from flask_login import LoginManager
from sqlalchemy.sql import text
import json


productsTemplate = 'products.html'

stock_view = Blueprint("stock_view", __name__)

def search_engine(query):
    product_list = {"Products":[]}
    if query:
        search_results = Product.query.whoosh_search(query)

    else:
        search_results = Product.query.order_by(Product.id)

    for r in search_results:
        product_name = str(r)
        product_list["Products"].append({"name": product_name[1:-1], "columns": [
            r.id,
            r.name,
            r.group,
            r.quantity,
            r.price]})

    return product_list


def columns_tr(model):
    columns = {}
    product_columns = model.__table__.columns.keys()
    columns["Columns"] = product_columns
    return columns


@stock_view.route('/products', methods=['GET', 'POST'])
def products():
    return render_template(productsTemplate)


@stock_view.route('/search', methods=['POST', 'GET'])
def search():
    query = request.args.get('search')
    pass

@stock_view.route('/stock', methods=['GET', 'POST'])
def stock():
    products_columns = columns_tr(Product)
    searched_products = search_engine(query=None)

    return render_template(productsTemplate, searched_products=searched_products, products_columns=products_columns)

