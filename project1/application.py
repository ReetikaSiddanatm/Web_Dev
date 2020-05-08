import os

from flask import Flask, session,url_for,redirect,jsonify,json
from flask import Flask,render_template,request,flash
from flask_session import Session
from sqlalchemy import create_engine,or_
from sqlalchemy.orm import scoped_session, sessionmaker
from flask_sqlalchemy import SQLAlchemy
from model import *
from imports import *
from Book_Details import *
from database import *
from  datetime import datetime
from Goodreads_api import *



  
app = Flask(__name__)
app.secret_key = "secret"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
db1.init_app(app)

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
        info = " , For another book please login again"
        
        return 'Logged in as ' + username + info + '<br>' + \
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
    pswd  = request.form.get("password")
       
    try:
        Member = db.session.query(Registartion).filter(Registartion.Email == email).all()
        if len(Member) >0 :
            
            print(len(Member))
            print(Member[0].Password)
            if Member[0].Email == email and Member[0].Password == pswd:
                print(Member[0].Firstname)
                session['username'] = request.form.get("Email")
                return  render_template("Search.html")
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
    pswd  = request.form.get("password")
    register = Registartion(Firstname =  name ,Email=email,Password = pswd,datetime = str(datetime.now()))
    
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


#############################  SEARCH WOTHOUT USING API ############################################


@app.route('/Search',methods=["GET","POST"])
def search():
    
    
        if request.method == "GET":
            return render_template("userHome.html")
        print("searching")
        search = request.form.get("search")
        # isbn = request.form.get("isbn")
        # title = request.form.get("book name")
        # author = request.form.get("Author")
        print(type(search))
        ##  Using Like Operator 
      
        if request.form.get("isbn") == "option1":
            print(search+" like  "+"isbn")
            book_search = Books.query.filter(Books.isbn.like('%'+search+'%')).all()
            #book_search = db1.session.query(Books).filter((Books.isbn.like('%'+search+'%')))
            print(book_search)
            
            
            
                # By title 
        elif request.form.get("book name") == "option2":
            print(search+" like   "+"book name")
            book_search = db1.session.query(Books).filter((Books.tittle.like('%'+search+'%'))).all()
            print(book_search)
           
                    
            # user is searching by author name
        elif request.form.get("Author") == "option3":
            print(search+" like   "+"author")
            book_search = db1.session.query(Books).filter((Books.author.like('%'+search+'%'))).all()
            print(book_search)
          
                
        else:
            print("wrong")
            return render_template("error.html", errors = "Sorry the details given doesnt match")
        
        if (len(book_search) > 0):
                return render_template("Search.html", books = book_search)
        else :
                return render_template("error.html", errors = "Sorry the details given doesnt match")
       
        
           # By giving the complete details
        # print("By details") 
      
        # s = db1.session.query(Books).filter(or_(Books.isbn==isbn,Books.tittle==title,Books.author==author)).all()
        # print(s)
        # if (len(s)!= 0):    
        #     return render_template("list of books.html",books = s)
        # else:
        #     return render_template("error.html", errors = "Sorry the details given doesnt match")


    
    
######################### SEARCH API IS IMPLEMENTED HERE #######################################

@app.route("/api/Search",methods = ["POST"])
def Search_api():
    try :

        if (not request.is_json) :
            return jsonify({"error" : "not a json request"}), 400

        reqData = request.get_json()

        if "search" not in reqData:
            return jsonify({"error" : "missing search param"}), 400
            
        value = reqData.get("search")
        print(value)

        if len(value) == 0 :
            return jsonify({"error" : "no results found"}), 404

           

        
        query = "%"+ value+"%"
        print(query)
        books = Books.query.filter(or_(Books.isbn.like(query), Books.tittle.like(query), Books.author.like(query)))
        print(books)
        try :

            books[0].isbn

            results = []

            for book in books :

                temp = {}

                temp["isbn"] = book.isbn
                temp["title"] = book.tittle
                temp["author"] = book.author
               
                results.append(temp)
            print(results)
            return jsonify({"books" : results}), 200

        except Exception as exc :

            return jsonify({"error" : "no results found"}), 404

    except Exception :
        return jsonify({"error" : "Server Error"}), 500
    
    
####################### WITHOUT USING API #####################  


@app.route("/books/<string:book_id>")
def book_details(book_id):

    # isbn = "0380795272"
    book = get_book(book_id)
    review=get_review(book_id)
    
    # book.isbn, book.name, book.author, book.year = db_session.execute("SELECT isbn, name, author, year FROM books WHERE isbn = :isbn", {"isbn": isbn}).fetchone()

    return render_template("Book_Page.html", Book=book[0],review=review)



#############################   USING API  #############################

@app.route("/api/book" , methods=["POST"])
def bookdetails():

    try:
        
        reqData = request.get_json()
        book_id= reqData.get("search")
        
        print(book_id)
        books = get_book(book_id)
        if books is None :
            return jsonify({"error" : "invalid isbn"})

        response = get_bookreads_api(book_id)
        r=response['books'][0]
        print(r)
        if (len(books)==0):
                return jsonify({"Error": "Invalid book ISBN"}), 404
        else:
            book = books[0]
            
            
            return jsonify({
                "title":book.tittle, 
                "author":book.author, 
                "isbn":book.isbn,
                "no_of_reviewers":r["reviews_count"],
                "rating":r["average_rating"]
                }) , 200
       
     
            
       

    except Exception as exe:
        print (exe)
        return jsonify({"error": "Server Error"}),404






@app.route("/review",methods = ["GET","POST"])
def add_review():

      if request.method == 'POST':
            try:

                  email = request.form.get("EMAIL")
                  print(email)
                  book=request.form.get('ISBN')
                  print(book)
                  text=request.form.get('review')
                  print(text)
                  rating=request.form.get('rating')
                  print(rating)
                  r = Review(userid= email,bookid= book,text = text, rating = rating)
                  print(r)
                  temp=list(request.form.items())
                  print(temp)
                  db.session.add(r)
                  db.session.commit()   
                  return render_template("review.html",message="Thankyou for ur feedback")
            except Exception:
                  return render_template("review.html",message="Already gave feedback")
      else :
            return render_template("review.html",message="Already gave feedback")
   




            
