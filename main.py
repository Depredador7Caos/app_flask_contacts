from flask import Flask
from app.auth import athentication
from app.auth.contactos.contactos import contact
from flask_sqlalchemy import SQLAlchemy
from app.auth.utils.db import db

import config
from config import DATABASE_CONNECTION_URI
app = Flask(__name__)

app.secret_key = "secret key"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_CONNECTION_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(athentication)
app.register_blueprint(contact)

db.init_app(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug = True)
