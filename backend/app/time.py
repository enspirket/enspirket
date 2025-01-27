# time.py

from flask import Blueprint, jsonify
import datetime
from app import get_db_connection

bp = Blueprint('time', __name__)

# time API
@bp.route('/api/time')
def time_API():
    # current_time = datetime.datetime.now()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''(SELECT NOW())''')
    current_time = cursor.fetchall()
    conn.close()
    
    return jsonify(current_time)