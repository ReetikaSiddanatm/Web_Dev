import os

from flask import Flask, render_template, request

  # Import table definitions.
from model import *
# from samp import *

app = Flask(__name__)

  # Tell Flask what SQLAlchemy databas to use.
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

  # Link the Flask app with the database (no Flask app is actually being run yet).
db.init_app(app)
# class Review(db.Model):
#     __tablename__ = "reviews"
#     # id = db.Column(db.Integer, primary_key=True)
#     userid = db.Column(db.String, nullable=False, primary_key=True)
#     bookid = db.Column(db.String,  primary_key=True)
#     text = db.Column(db.String, nullable = True)
#     rating = db.Column(db.String, nullable = False)

def main():
    # Create tables based on each table definition in `models`
  db.create_all()
# def query():
  
  #Member = Registartion.query.get()
  # print(Member[0].Email)
  

if __name__ == "__main__":
    # Allows for command line interaction with Flask application
  with app.app_context():
    main()