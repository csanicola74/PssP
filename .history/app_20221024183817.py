from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
# load python-dotenv
from dotenv import load_dotenv
import os

load_dotenv()

mysql_username = os.getenv("MYSQL_USERNAME")
mysql_password = os.getenv("MYSQL_PASSWORD")
mysql_host = os.getenv("MYSQL_HOST")

db = SQLAlchemy()
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://' + mysql_username + \
    ':' + mysql_password + '@' + mysql_host + ':3306/patient_portal'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# required by mysql for every flask connection to it; just a dummy variable can be used
app.secret_key = '343fdksjf34#$#dfjkhdf0SDJH0df9fd98343fdfu34rf'

db.init_app(app)

# a model window is a window that hovers inside a window
