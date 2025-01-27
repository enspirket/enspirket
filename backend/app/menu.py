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
    cursor.execute('''(SELECT *
                        FROM product
                        JOIN price ON product.price_id = price.price_id)''')
    db = cursor.fetchall()
    conn.close()
    
    return jsonify(db)

# @bp.route('/api/menu_item')
# def menu_item_API():
#     conn = get_db_connection()
#     cursor = conn.cursor()
#     cursor.execute('''(SELECT *
#                         FROM product
#                         JOIN price ON product.price_id = price.price_id
#                         WHERE product.product_id = %s)''')
#     db = cursor.fetchall()
#     conn.close()
    
#     return jsonify(db)