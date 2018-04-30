from sqlite3 import IntegrityError

from flask import render_template, redirect, url_for, Blueprint
from flask_login import login_user, login_required, logout_user, current_user
from forms import LoginForm, SignupForm
from models import User, db
from sqlalchemy.exc import IntegrityError
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy import asc
from flask_login import LoginManager

baseTemplate = 'index.html'
loginTemplate = 'login.html'
signupTemplate = 'signup.html'

stock_manager = Blueprint("stock_manager", __name__)

login_manager = LoginManager()



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@stock_manager.route('/', methods=['GET'])
def index():
    return render_template(baseTemplate)

@stock_manager.route('/navitem1', methods=['GET'])
@login_required
def navitem1():
    return render_template(baseTemplate)

@stock_manager.route('/navitem2', methods=['GET'])
def navitem2():
    return redirect(url_for('stock_manager.index'))

@stock_manager.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()

        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return render_template(baseTemplate, loggingMessage='Logged in successfully as '+current_user.username)

        return render_template(loginTemplate, form=form, error=True)

    return render_template(loginTemplate, form=form)

@stock_manager.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        try:
            hashed_password = generate_password_hash(form.password.data, method='sha256')
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            return render_template(signupTemplate, form=form, success=True)
        except IntegrityError as e:
            return render_template(signupTemplate, form=form, error=e)

    return render_template(signupTemplate, form=form)

@stock_manager.route('/logout')
@login_required
def logout():
    logout_user()
    return render_template(baseTemplate, loggingMessage='Logged out successfully')
