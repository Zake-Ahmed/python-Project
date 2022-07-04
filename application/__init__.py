from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\  
           'sqlite:///' + os.path.join(basedir, 'data.db') #os.getenv('DATABASE_URI')
           #to connect to the cloud database use this syntax "mysql+pymysql://username:password@host/database_name"
                                                            #Also us the export function so both the secret key and the database links are not pushed up to github
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "shhhhh" # os.getenv('SECRET_KEY')

db = SQLAlchemy(app)

from application import routes