import os

from flask import Flask, session,url_for,redirect
from flask import Flask,render_template,request,flash
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from model import *
from Book_Details import *
from  datetime import datetime  
app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
from database import *
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
    #Registartion.query.all()
    name = request.form.get("fname")
    email = request.form.get("Email")
    pswd  = request.form.get("password")
       
    try:
        Member = db.session.query(Registartion).filter(Registartion.Email == email).all()
        if len(Member) >0 :
            
            print(len(Member))
            print(Member[0].Password)
            if Member[0].Email == email and Member[0].Password == pswd:
                print(Member[0].Firstname)
                session['username'] = request.form.get("Email")
                return redirect(url_for('indexed'))   
            else:
                return render_template("error.html", errors = " Username / Password is incorrect")
        else:
            return "<h1> Please Login / Register </h1>" 
       
    
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
@app.route('/search')
def search():
   # remove the username from the session if it is there
   book=get_book_author("Susan Cooper")
   return render_template("Result.html",book=book)
@app.route("/books/<string:book_id>")
def book_details(book_id):

    # isbn = "0380795272"
    book = get_book(book_id)
    review=get_review(book_id)
    
    # book.isbn, book.name, book.author, book.year = db_session.execute("SELECT isbn, name, author, year FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()

    return render_template("Book_Page.html", Book=book[0],review=review)

# @app.route("/review",methods = ["GET","POST"])
# def add_review():

#       if request.method == 'POST':
#         email = request.form.get("EMAIL")
#         book=request.form.get('ISBN')
#         text=request.form.get('review')
#         rating=request.form.get('rating')
#         # print(rating)
#         r = Review(userid= email,bookid= book,text = text, rating = rating)
#         # print(r)
#         db.session.add(r)
#         db.session.commit()
#         return render_template("review.html",message="Thankyou for ur feedback")
      
#       else :
#         return redirect(url_for("add_review"))
 

  



   


            
