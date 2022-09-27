from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

db = 'truck_history'

class Truck:
    def __init__(self, data):
        self.id = data['id']
        self.product = data['product']
        self.truckNum = data['truckNum']
        self.rate = data['rate']
        self.date = data['date']
        self.origin = data['origin']
        self.destination = data['destination']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM trucks;"
        results = connectToMySQL(db).query_db(query)
        trucks = []
        for truck in results:
            trucks.append(cls(truck))
        return trucks

    @classmethod
    def get_search(cls, data):
        query = "SELECT * FROM trucks WHERE origin=%(origin)s AND destination=%(destination)s ORDER BY RIGHT (date, 2) DESC;"
        results = connectToMySQL(db).query_db(query, data)
        trucks = []
        for truck in results:
            trucks.append(cls(truck))
        return trucks