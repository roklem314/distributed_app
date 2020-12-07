import os
import secrets
from functools import wraps
from flask import Flask
from os import urandom
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

if os.environ.get("HEROKU"): #running at HEROKU
    app.config["SECRET_KEY"] = secrets.token_bytes(42)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    app.config["SQLALCHEMY_ECHO"] = False

else: #running at LOCALHOST
    app.config["SECRET_KEY"] = urandom(42)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///encrypter.db"
    app.config["SQLALCHEMY_ECHO"] = True

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = urandom(32)
db = SQLAlchemy(app)


# needed imports to use app
from application import views

from application import models
from application import views

# luodaan taulut tietokantaan tarvittaessa ja
if not os.environ.get("HEROKU"):
    try:
        db.create_all()
    except:
        pass
