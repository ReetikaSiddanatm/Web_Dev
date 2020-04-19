import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from model import *
from  datetime import datetime



  
app = Flask(__name__)
app.secret_key = "secret"
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



@app.route('/')
def indexed():
    if 'username' in session:
        username = session['username']
        return 'Logged in as ' + username + '<br>' + \
         "<b><a href = '/logout'>click here to log out</a></b>"
    return "You are not logged in <br><a href = '/login'></b>" + \
      "click here to log in</b></a>"
  

@app.route("/register")
def index():    
    return render_template("Registartion.html")
 
  
@app.route("/auth",methods = ["GET","POST"])
def authenticate():
    Registartion.query.all()
    name = request.form.get("fname")
    email = request.form.get("Email")
    
    try:
        Member = db.session.query(Registartion).filter(Registartion.Email == email).all()
        print(Member[0].Firstname)
        session['username'] = request.form.get("Email")
        return redirect(url_for('indexed'))   
    
    except Exception :
	    return render_template("error.html", errors = "Details are already given")
        
    
@app.route("/User",methods = ["GET","POST"])
def User():
    
    Registartion.query.all()
    name = request.form.get("fname")
    email = request.form.get("Email")
    register = Registartion(Firstname =  name ,Email=email,datetime = str(datetime.now()))
    
    try:
        db.session.add(register)
        db.session.commit()
        return render_template("User.html",f=name,email = email)
        
    except Exception :
	    return render_template("error.html", errors = "Details are already given")
 


@app.route("/admin")

def Member():
      """List all users."""
     
      Member = Registartion.query.all()
      return render_template("show.html", Member=Member)
      
      
@app.route('/logout')
def logout():
   # remove the username from the session if it is there
   session.pop('username', None)
   return redirect(url_for('index'))


    

  



   


            
