from sqlite3 import IntegrityError

from flask import render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from main import app, login_manager, db
from forms import LoginForm, SignupForm
from models import User, Product
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import asc

productsTemplate = 'products.html'


@app.route('/products', methods=['GET','POST'])
def products():
    return render_template(productsTemplate)

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#
#     return render_template(productsTemplate)

@app.route('/stock', methods=['GET','POST'])
def stock():
    searched_products = []
    query = request.args.get('query')
    if query:
        products = Product.query.order_by(Product.id)
        for product in products:
            if query in product.name:
                searched_products.append(product)
    else:
        products = Product.query.order_by(Product.id)

    return render_template(productsTemplate, products=products, searched_products=searched_products)

