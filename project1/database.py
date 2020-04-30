import os
import csv
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
#from models import Book
from sqlalchemy import Column, Integer, String,DateTime,exists,Sequence
from flask import Flask
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


# Import table definitions.

app = Flask(__name__)

# Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.app_context().push()
# Link the Flask app1 with the database (no Flask app1 is actually being run yet).     

db = SQLAlchemy()

class Review(db.Model):
    __tablename__ = "reviews"
    userid = db.Column(db.String, nullable = False)
    bookid = db.Column(db.String, primary_key=True)
    text = db.Column(db.String, nullable = True)
    rating = db.Column(db.Integer, nullable= False)

db.init_app(app)
db.create_all()

def get_review(book_id):
    review=db.session.query(Review).filter(Review.bookid == book_id).all()    
    return review

def main():
    pass
    #    db.session.add(Review(userid ="sravya@gmail.com",bookid="1416949674",text="Bad",rating=1))
    #    db.session.commit()

if __name__ == "__main__":
        main()
       