from sqlalchemy import asc
from flask import render_template
from flask import session as login_session
from RestaurantApp import Restaurant
from RestaurantApp import app
from RestaurantApp import session


@app.route('/')
@app.route('/restaurant/')
def showRestaurants():
    restaurants = session.query(Restaurant).order_by(asc(Restaurant.name))
    if 'username' not in login_session:
        return render_template('publicrestaurants.html', restaurants=restaurants)
    else:
        return render_template('restaurants.html', restaurants=restaurants)