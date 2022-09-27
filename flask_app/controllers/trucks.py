from flask import render_template, flash, redirect, request, session
from flask_app import app
from flask_app.models.truck import Truck

@app.route('/truck_history')
def truck_history():
    trucks = Truck.get_all()
    return render_template('truck_history.html', trucks = trucks)


@app.route('/truck_search', methods=['POST'])
def truck_search():
    data = {
        'origin' : request.form['origin'],
        'destination' : request.form['destination']
    }
    trucks = Truck.get_search(data)
    return render_template('truck_search.html', trucks = trucks)