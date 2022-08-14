import bcrypt
import psycopg2
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY']='thisisfirstflaskapp'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://aquovfvhnxfhww:3b01116fb023f893d0fc1eba91b6edf019429c2d8146c9fc2370f2ecb84beccd@ec2-44-206-89-185.compute-1.amazonaws.com:5432/d6qoa1cvmeobhb'


conn = psycopg2.connect(
   database="d6qoa1cvmeobhb", user='aquovfvhnxfhww', password='3b01116fb023f893d0fc1eba91b6edf019429c2d8146c9fc2370f2ecb84beccd', host='ec2-44-206-89-185.compute-1.amazonaws.com'
)
cursor = conn.cursor()

db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
from final_flask import routes
