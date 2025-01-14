# menu.py

from flask import Blueprint, jsonify
import pymysql
from app import get_db_connection

# Create a blueprint for the routes
bp = Blueprint('menu', __name__)

# Menu API
@bp.route('/api/menu')
def menu_API():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''(select * from drinks join price on drinks.drink_price_id = price.price_id)
                     union (select * from combos join price on combos.combo_price_id = price.price_id) 
                     union (select * from snacks join price on snacks.snack_price_id = price.price_id)''')
    db = cursor.fetchall()
    conn.close()
    
    return jsonify(db)