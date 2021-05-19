from flask import render_template
from app import app
from app.models.orders_list import orders
from app.models.items_list import items
from app.static import *


@app.route('/order')
def index():
    return render_template('index.html', title='Home',orders=orders, item=items)