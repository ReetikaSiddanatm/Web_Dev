import os
from flask import Flask,render_template,request,flash
# from flask_session import Session
# from sqlalchemy import create_engine
# from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from flask import Flask

# app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# app.app_context().push()
db2 = SQLAlchemy()
class Review(db2.Model):
    __tablename__ = "reviews"
    # id = db.Column(db.Integer, primary_key=True)
    userid = db2.Column(db2.String, primary_key=True)
    bookid = db2.Column(db2.String,  primary_key=True)
    text = db2.Column(db2.String, nullable = True)
    rating = db2.Column(db2.Integer, nullable = False)




  # Link the Flask app with the database (no Flask app is actually being run yet).
# db2.init_app(app)
# def get_dbinstance():
#     return db2
# def main():
    # book = Review(userid="sravs@gmail.com",bookid=1416949658,text="good",rating=5)
    # db2.session.add(book)
    # db2.session.commit()
    # Create tables based on each table definition in `models`
    # db2.create_all()
# def query():
  
  #Member = Registartion.query.get()
  # print(Member[0].Email)
  

# if __name__ == "__main__":
#     # Allows for command line interaction with Flask application
#   with app.app_context():
#     main()