import os

from flask import Flask, render_template, redirect, url_for, request
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from data import db_session
from data.users import User
from data.items import Item
from forms.RegistrForm import RegisterForm
from forms.LoginForm import LoginForm
from forms.ItemForm import ItemForm
from flask_sqlalchemy import SQLAlchemy
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'bazarvito_secret_key'
app.config['UPLOAD_FOLDER'] = 'static/img'
login_manager = LoginManager()
login_manager.init_app(app)
db_session.global_init("db/users.db")


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    con = sqlite3.connect('db/main.db')
    cur = con.cursor()
    data = list(cur.execute('select * from all_offers'))
    con.close()
    return render_template('index.html', title='Bazarvito',
                           current_user=current_user if current_user.is_authenticated else False, data=data)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('registr_form.html', title='Регистрация',
                                   form=form,
                                   message="Пароли не совпадают")
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('registr_form.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть")
        if '+' not in form.phone_number.data:
            return render_template('registr_form.html', title='Регистрация',
                                   form=form,
                                   message="Номер телефона ввёден неправильно")
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            email=form.email.data,
            phone_number=form.phone_number.data
        )
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('registr_form.html', title='Регистрация', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect(request.args.get("next") or url_for("profile"))
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@app.route('/additem', methods=['GET', 'POST'])
@login_required
def additem():
    form = ItemForm()
    if form.validate_on_submit():
        name = form.name.data
        price = form.price.data
        adress = form.adress.data
        description = form.description.data
        img = request.files['img']
        if img:
            filename = os.path.join('static/img/', img.filename)
            img.save(filename)
        else:
            filename = 'base.jpg'

        con = sqlite3.connect('db/main.db')
        cur = con.cursor()
        cur.execute('INSERT INTO all_offers (name, description, adress, price, img) VALUES (?, ?, ?, ?, ?)',
                    (name, description, adress, int(price), img.filename))
        con.commit()
        con.close()
        return redirect('/additem')
    return render_template('additem.html', form=form)


if __name__ == '__main__':
    # create_db()
    app.run(host='127.0.0.1', port=8080)
