# cart.py

from dataclasses import dataclass
from flask import session, Blueprint, jsonify, request
from app import get_db_connection

@dataclass
class Product:
    product_id : str
    product_size : str
    product_toppings : list
    product_ice : str
    product_price : float
    product_quantity : int

bp = Blueprint('cart', __name__)

@bp.route('/api/cart', methods=['GET'])
def view_cart_API():
    cart = session.get('cart', {})
    if not cart:
        return jsonify({"message":"Your cart is empty."}), 200
    return jsonify(session['cart']), 200


@bp.route('/api/add_to_cart', methods=['POST'])
def add_to_cart_API():
    if 'cart' not in session:
        session['cart'] = []

    data = request.get_json()

    product_id = data.get('product_id')
    product_name = data.get('product_name')
    product_size = data.get('product_size')
    product_toppings = data.get('toppings')
    product_ice = data.get('ice')
    product_price = float(data.get('product_price'))
    product_quantity = int(data.get('product_quantity'))
    
    item = Product(product_id, product_size, product_toppings, product_ice, product_price, product_quantity)

    session['cart'].append(item)

    session.modified = True
    
    return jsonify({"message":"Item added to cart."}), 200


@bp.route('/api/remove_from_cart', methods=['POST'])
def remove_from_cart_API():

    position = request.get_json()

    position = int(position.get('position'))

    if position >= 0 and position < len(session['cart']):
        session['cart'].pop(position)

    session.modified = True
    
    return jsonify({"message":"Item removed to cart."}), 200


@bp.route('/api/empty_cart', methods=['POST'])
def empty_cart_API():
    session['cart'].clear()

    session.modified = True
    
    return jsonify({"message":"Item removed to cart."}), 200
    



