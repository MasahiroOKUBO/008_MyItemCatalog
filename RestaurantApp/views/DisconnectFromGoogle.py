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


@app.route('/disconnect_from_google')
def disconnect_from_google():
    if not 'session' in request.cookies:
        print 'login_session is maybe None'
        response = make_response(json.dumps('Session does not exists in Cookie.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    if not login_session.has_key('access_token'):
        print 'login_session does not have access_token'
        response = make_response(json.dumps('login_session does not have access_token.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    print login_session.keys()
    access_token = login_session['access_token']
    if access_token is None:
        print 'Access Token is None'
        response = make_response(json.dumps('Access Token is None'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # print login_session['credentials'].access_token
    print 'In disconnect access token is %s', login_session['access_token']
    print 'User name is: '
    print login_session['username']
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print 'result is '
    print result
    if result['status'] == '200':
        del login_session['credentials']
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']
        del login_session['state']
        del login_session['user_id']
        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response
    else:
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response
