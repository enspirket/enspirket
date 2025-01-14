# cart.py


from flask import session, Blueprint, jsonify, request
from app import get_db_connection
# from flask_session import Session

bp = Blueprint('cart', __name__)


@bp.route('/api/cart', methods=['GET'])
def view_cart_API():
    cart = session.get('cart', {})
    if not cart:
        return jsonify({"message":"Your cart is empty."}), 200



    return jsonify(session['cart']), 200


@bp.route('/api/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'cart' not in session:
        session['cart'] = []

    data = request.get_json()

    product_id = data.get('product_id')

    session['cart'].append(product_id)

    session.modified = True
    
    return jsonify({"message":"Item added to cart."}), 200


@bp.route('/api/remove_from_cart', methods=['POST'])
def remove_from_cart():

    position = request.get_json()

    position = int(position.get('position'))

    if position >= 0 and position < len(session['cart']):
        session['cart'].pop(position)

    session.modified = True
    
    return jsonify({"message":"Item removed to cart."}), 200


@bp.route('/api/empty_cart', methods=['POST'])
def empty_cart():
    session['cart'] = []

    session.modified = True
    
    return jsonify({"message":"Item removed to cart."}), 200
    



