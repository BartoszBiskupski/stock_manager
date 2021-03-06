from sqlite3 import IntegrityError

from flask import render_template, redirect, url_for, request, Blueprint
# from flask_login import login_user, login_required, logout_user, current_user
# from main import app, login_manager
# from forms import LoginForm, SignupForm
from models import Product, db
# from sqlalchemy.exc import IntegrityError
# from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import asc
from flask_login import LoginManager

productsTemplate = 'products.html'

stock_view = Blueprint("stock_view", __name__)



@stock_view.route('/products', methods=['GET','POST'])
def products():
    return render_template(productsTemplate)

# @app.route('/search', methods=['GET', 'POST'])
# def search():
#
#     return render_template(productsTemplate)

@stock_view.route('/stock', methods=['GET','POST'])
def stock():
    searched_products = []
    query = request.args.get('query')
    search_range = request.args.get('searchrange')

    if True:
        products = Product.query.order_by(Product.id)
        if search_range == "all":
            for product in products:
                if query in product.name or query == str(product.id) or query in product.group:
                    searched_products.append(product)
        elif search_range == "name":
            for product in products:
                if query in product.name:
                    searched_products.append(product)
        elif search_range == "id":
            for product in products:
                if query == str(product.id):
                    searched_products.append(product)
        elif search_range == "group":
            for product in products:
                if query in product.group:
                    searched_products.append(product)



    return render_template(productsTemplate, products=products, searched_products=searched_products)

