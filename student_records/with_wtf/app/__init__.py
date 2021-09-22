from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
app.config['SECRET_KEY'] = 'example-secret' #Used for demonstration, not in production

db = SQLAlchemy(app)

from app import routes