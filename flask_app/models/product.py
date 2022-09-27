from flask_app import app
from flask import flash
import re
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
from flask_app.config.mysqlconnection import connectToMySQL


db = 'lookfor'

class Product:
    def __init__(self, data):
        self.id = data['id']
        self.location = data['location']
        self.category = data['category']
        self.fupc = data['fupc']
        self.bupc = data['bupc']
        self.description = data['description']
        self.pack = data['pack']
        self.size = data['size']
        self.ads = data['ads']
        self.fcst = data['fcst']
        self.qty = data['qty']
        self.manufacturer = data['manufacturer']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM products LIMIT 2000;"
        results = connectToMySQL(db).query_db(query)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def search_upc(cls, data):
        query = "SELECT * FROM products WHERE fupc=%(fupc)s ORDER BY bupc;"
        results = connectToMySQL(db).query_db(query, data)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def best_sellers(cls):
        query = "SELECT * FROM products WHERE qty > 2000 AND category <> 'PROD' AND category <> 'HBC' AND category <> 'DELI' AND category <> 'FREMT' AND category <> 'FRESF' AND category <> 'FZSFD' AND category <> 'TBCO' AND category <> 'BK' AND category <> 'GM' AND category <> 'FRZ' AND category <> 'DAIRY' AND manufacturer <> 'C&S WHOLESALE GROCERS INT' ORDER BY qty DESC"
        results = connectToMySQL(db).query_db(query)
        products = []
        for product in results:
            products.append(cls(product))
        return products

    @classmethod
    def ic(cls):
        query = "SELECT * FROM products WHERE category = 'IC' AND qty > 750 ORDER BY qty DESC;"
        results = connectToMySQL(db).query_db(query)
        products = []
        for product in results:
            products.append(cls(product))
        return products