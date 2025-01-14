# auth.py

from app import get_db_connection
from flask import session, request, jsonify, Blueprint
# from flask_login import LoginManager


bp = Blueprint('auth', __name__)

@bp.route('/api/login', methods=['GET', 'POST'])
def login_API():
    
    
    pass
    # if request.method == 'GET':
    #     email = request.json.get("email")
    #     password = request.json.get("password")
        

    #     if not (password and email):
    #         return jsonify({'message': 'All fields required'}), 401
    #     print(email, password)
    #     conn = get_db_connection()
    #     cursor = conn.cursor()
    #     cursor.execute('SELECT email FROM customer WHERE email = %s and password = %s', (email, password))
    #     db = cursor.fetchall()
    #     conn.close()
        
    #     if db:
    #         return jsonify({'message': 'Wrong information'}), 409

    #     return jsonify({'message': 'User successfully login'}), 201
