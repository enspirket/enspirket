# __init__.py

from flask import Flask
import pymysql
from flask_session import Session
from flask_cors import CORS


pymysql.install_as_MySQLdb()

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',        # your MySQL host
        user='root',             # your MySQL username
        password='m@c0smy5ql',     # your MySQL password
        database='test',     # your MySQL database name
        cursorclass=pymysql.cursors.DictCursor  # Return results as dictionaries
    )
    return connection


def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    app.config['SESSION_PERMANENT'] = False
    CORS(app)
    Session(app)
    

    from . import menu
    from . import auth
    from . import cart
    from . import time
    from . import checkout
    app.register_blueprint(menu.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(cart.bp)
    app.register_blueprint(time.bp)
    app.register_blueprint(checkout.bp)

    return app