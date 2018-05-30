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
from sqlalchemy.dialects.postgresql import TSVECTOR
from sqlalchemy import select, cast
from sqlalchemy_searchable import search



productsTemplate = 'products.html'
stock_view = Blueprint("stock_view", __name__)


def search_engine(query):
    product_list = {"Products":[]}
    if query:
        search_results = Product.query.order_by(Product.id)
        search_results = search(search_results, query)

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
    products_columns = columns_tr(Product)
    if request.method == "POST":
        searched_products = search_engine(query=request.form.get('query'))
        return render_template(productsTemplate, searched_products=searched_products, products_columns=products_columns)


@stock_view.route('/stock', methods=['GET', 'POST'])
def stock():
    products_columns = columns_tr(Product)
    searched_products = search_engine(query=None)

    return render_template(productsTemplate, searched_products=searched_products, products_columns=products_columns)

@stock_view.route('/stock/add', methods=["POST"])
def add_stock():
    new_product = Product(
        name=request.form.get("product_name"),
        group=request.form.get("product_group"),
        quantity=request.form.get("product_quantity"),
        price=request.form.get("product_price"),
    )
    db.session.add(new_product)
    db.session.commit()
    return redirect(url_for('stock_view.stock'))
