import httplib2
import json
import random
import requests
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from sqlalchemy import create_engine
from sqlalchemy import asc
from sqlalchemy.orm import sessionmaker
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import jsonify
from flask import url_for
from flask import flash
from flask import make_response
from flask import session as login_session

from RestaurantApp import Base
from RestaurantApp import Restaurant
from RestaurantApp import Menu
from RestaurantApp import User
from RestaurantApp import app
from RestaurantApp import session

def getUserInfo(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    return user


# Show a restaurant menu
@app.route('/restaurant/<int:restaurant_id>/')
@app.route('/restaurant/<int:restaurant_id>/menu/')
def showMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    creator = getUserInfo(restaurant.user_id)
    items = session.query(MenuItem).filter_by(
        restaurant_id=restaurant_id).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('publicmenu.html',
                               items=items,
                               restaurant=restaurant,
                               creator=creator)
    else:
        return render_template('menu.html', items=items, restaurant=restaurant, creator=creator)
