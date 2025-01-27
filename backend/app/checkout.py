# checkout.py

from flask import session, Blueprint, jsonify, request
from app import get_db_connection
# from flask_session import Session

bp = Blueprint('checkout', __name__)


@bp.route('/api/total', methods=['GET'])
def view_cart_API():
    cart = session.get('cart', {})
    if not cart:
        return jsonify({"message":"Your cart is empty."}), 200
    else:
        total = 0
        for item in cart:
            total += item.product_price * item.product_quantity
            for topping in item.product_toppings:
                total += float(topping["price"])
        return jsonify({"total":total}), 200


# price of each item