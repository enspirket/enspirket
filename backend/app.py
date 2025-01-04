from flask import Flask,render_template, request
import pymysql
# from flask_mysqldb import MySQL
pymysql.install_as_MySQLdb()


app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


# Home page route
@app.route('/')
def index():
    return render_template('index.html')

