from flask_app import app
from flask import render_template, request, redirect, session, flash
from flask_app.models.user import User
from flask_app.models.product import Product
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/process', methods=["POST"])
def process():
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password'],
        'confirm_password' : request.form['confirm_password'],
    }
    valid = User.user_validator(data)

    if valid:
        pw_hash = bcrypt.generate_password_hash(request.form['password'])
        data['pw_hash'] = pw_hash
        user = User.create_user(data)
        session['user_id'] = user
        return redirect('/user/success')
    return redirect('/')

@app.route('/user/login', methods=['POST'])
def user_login():
    user = User.get_by_email(request.form)
    if not user:
        flash('Invalid email or password')
        return redirect('/')
    if not bcrypt.check_password_hash(user.password, request.form['password']):
        flash('Invalid email or password')
        return redirect('/')
    session['user_id'] = user.id
    return redirect('/user/success')

@app.route('/user/success')
def success():
    if 'user_id' not in session:
        return redirect('/')

    products = Product.get_all()
    return render_template('success.html', products = products)


@app.route('/fupc')
def fupc():
    products = Product.get_fupc()
    return render_template('fupc.html', products = products)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')