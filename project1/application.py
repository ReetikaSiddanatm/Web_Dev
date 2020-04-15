import os

from flask import Flask, session
from flask import Flask,render_template,request
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))

# @app.route("/register")
# def index():
#     return render_template("Registartion.html")

@app.route("/")
def index():
     return render_template("Registartion.html")
 
@app.route("/User",methods = ["GET","POST"])
def user():
 
    f = request.form.get("fname")
    l  = request.form.get("lname")
    print(f + " "+ l)
    return render_template("User.html",first = f,last = l)
            
