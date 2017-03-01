from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash
from flask import make_response
from flask import session as login_session

from RestaurantApp import Restaurant
from RestaurantApp import Menu
from RestaurantApp import User
from RestaurantApp import app, session


@app.route('/restaurant/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu(restaurant_id, menu_id):
    if 'username' not in login_session:
        return redirect('/login')
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    item_to_delete = session.query(Menu).filter_by(id=menu_id).one()
    if login_session['user_id'] != restaurant.user_id:
        js_snippet = '''
        <script>function myFunction() {alert('You are not authorized to delete menu items to this restaurant.
        Please create your own restaurant in order to delete items.');}</script><body onload='myFunction()''>
        '''
        return js_snippet
    if request.method == 'POST':
        session.delete(item_to_delete)
        session.commit()
        flash('Menu Item Successfully Deleted')
        return redirect(url_for('showMenu', restaurant_id=restaurant_id))
    else:
        return render_template('form-deletemenu.html', item=item_to_delete)
