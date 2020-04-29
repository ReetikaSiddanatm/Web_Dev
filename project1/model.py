from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Registartion(db.Model):
    __tablename__ = "Registartion"
    Firstname = db.Column(db.String, nullable=False)
    Email = db.Column(db.String, primary_key=True)
    Password = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String,nullable= False)
    


db = SQLAlchemy()
class Review(db.Model):
    __tablename__ = "reviews"
    # id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, primary_key=True)
    bookid = db.Column(db.String,  primary_key=True)
    text = db.Column(db.String, nullable = True)
    rating = db.Column(db.Integer, nullable = False)