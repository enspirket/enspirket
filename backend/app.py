from flask import Flask
import pymysql

# Use PyMySQL as a drop-in replacement for MySQLdb
pymysql.install_as_MySQLdb()

app = Flask(__name__)

def get_db_connection():
    connection = pymysql.connect(
        host='localhost',        # your MySQL host
        user='root',             # your MySQL username
        password='',     # your MySQL password
        database='',     # your MySQL database name
        cursorclass=pymysql.cursors.DictCursor  # Return results as dictionaries
    )
    return connection

# Home page route
@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''(select * from drinks join price on drinks.drink_price_id = price.price_id)
                     union (select * from combos join price on combos.combo_price_id = price.price_id) 
                     union (select * from snacks join price on snacks.snack_price_id = price.price_id)''')
    db = cursor.fetchall()
    conn.close()
    return db

if __name__ == '__main__':
    app.run(debug=True)