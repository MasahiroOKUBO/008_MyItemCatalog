import random
import string
from flask import session as login_session
from flask import render_template

from RestaurantApp import app

@app.route('/login')
def showLogin():
    # def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    login_session['state'] = state
    return render_template('page-login.html', STATE=state)