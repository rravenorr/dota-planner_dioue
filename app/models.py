from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import bcrypt

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    _password = db.Column(db.String(60), nullable=False)  # Store the hashed password
    teams = db.relationship('Team')

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password  # Automatically hash the password using the property setter

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, plaintext_password):
        # Hash the plaintext password using bcrypt before storing it
        self._password = bcrypt.hashpw(plaintext_password.encode('utf-8'), bcrypt.gensalt())

    def check_password(self, plaintext_password):
        # Check if the provided password matches the stored hashed password
        return bcrypt.checkpw(plaintext_password.encode('utf-8'), self._password)


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String(60), nullable=False, unique=True)
    logo_url = db.Column(db.String(255))  # Assuming a maximum URL length of 255 characters
    team_number = db.Column(db.Integer, unique=True, nullable=False)
    carry = db.Column(db.String(30), nullable=False, unique=True)
    midlaner = db.Column(db.String(30), nullable=False, unique=True)
    offlaner = db.Column(db.String(30), nullable=False, unique=True)
    soft_support = db.Column(db.String(30), nullable=False, unique=True)
    hard_support = db.Column(db.String(30), nullable=False, unique=True)

    def __init__(self, team_name, logo_url, team_number, carry, midlaner, offlaner, soft_support, hard_support):
        self.team_name = team_name
        self.logo_url = logo_url
        self.team_number = team_number
        self.carry = carry
        self.midlaner = midlaner
        self.offlaner = offlaner
        self.soft_support = soft_support
        self.hard_support = hard_support
