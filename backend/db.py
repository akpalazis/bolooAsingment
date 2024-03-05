from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

class ShortURL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    long_url = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, nullable=True)  # Allow NULL values
    hits = db.Column(db.Integer, default=0)
    uniq_hits = db.Column(db.Integer, default=0)
    ips = db.Column(db.ARRAY(db.String(45)))  # Assuming IPv4 as strings
