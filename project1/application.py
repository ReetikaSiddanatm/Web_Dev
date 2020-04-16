import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from model import*
from  datetime import datetime



  
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

# Check for environment variable
# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# # Configure session to use filesystem
# app.config["SESSION_PERMANENT"] = False
# app.config["SESSION_TYPE"] = "filesystem"
# Session(app)

# Set up database
# engine = create_engine(os.getenv("DATABASE_URL"))
# ab = scoped_session(sessionmaker(bind=engine))


       
@app.route("/")
def index():    
    return render_template("Registartion.html")
 
      
 
@app.route("/User",methods = ["GET","POST"])
def user():
    
    Registartion.query.all()
    f = request.form.get("fname")
    email = request.form.get("Email")
    p = request.form.get("password")
    register = Registartion(Firstname = f,Email=email,datetime = datetime.now())
    try:
        db.session.add(register)
        db.session.commit()
        print(f+" "+email)
        return render_template("User.html",f=f,email = email)
    except Exception :
	    return render_template("error.html", errors = "Details are already given")


   


            
