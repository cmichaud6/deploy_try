from flask import render_template, flash, redirect, request, session
from flask_app import app
from flask_app.models.product import Product

@app.route('/search_upc', methods=['POST'])
def search_upc():
    data = {
        'fupc' : request.form['fupc']
    }
    products = Product.search_upc(data)
    return render_template('search_upc.html', products = products)

@app.route('/best_sellers')
def best_sellers():
    products = Product.best_sellers()
    return render_template('best_sellers.html', products = products)

@app.route('/ic')
def ic():
    products = Product.ic()
    return render_template('ic.html', products = products)