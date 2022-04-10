from flask import Flask
from flask_app import app
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow



    ############## Create Database ############
    db = SQLAlchemy(app)

    ############## Create Marshmallow ############
    marshmallow = Marshmallow(app)

    return db, marshmallow


