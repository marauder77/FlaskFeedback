from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

db = SQLAlchemy

def connect_db(app):

    db.app = app
    db.init_app(app)

class User(db.Model):

    __tablename__ = "Users"

    username = db.Column(db.String(20), primary_key=True, nullable=False, unique=True)
    password = db.Column(db.Text, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)

class Feedback(db.Model):

    __tablename__ = "Feedback"

    id = db.Column(db.Integer, unique=True, autoincrementing=True)
    title = db.Column(db.Text(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    username = db.Column(db.String(20), 
                        db.ForeignKey('users.username'),
                        nullable=False)