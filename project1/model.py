from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

class Registartion(db.Model):
    __tablename__ = "Registartion"
    Firstname = db.Column(db.String, primary_key=True)
    Email = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String,nullable= False)

class Book(db.Model):
    __tablename__ = "BOOK"
    isbn = db.Column(db.String, nullable = False,primary_key=True)
    tittle = db.Column(db.String, nullable = False)
    author = db.Column(db.String, nullable = False)
    year = db.Column(db.String, nullable= False)

# db.init_app(app)

# db1.create_all()



class Review(db.Model):
    __tablename__ = "reviews"
    # id = db.Column(db.Integer, primary_key=True)
    userid = db.Column(db.String, nullable=False)
    bookid = db.Column(db.String,  primary_key=True)
    text = db.Column(db.String, nullable = True)
    rating = db.Column(db.String, nullable = False) 

# class review(db.Model):
#     _tablename_ = "review"
#     userName = db.Column(db.String, nullable=False, primary_key=True)
#     book_id = db.Column(db.Integer, primary_key=True)
#     rating = db.Column(db.String, nullable=False)
#     feedback = db.Column(db.String(140),nullable=False)
#     def _init_(self,userName, book_id, rating, feedback) :
#         self.userName = userName
#         self.book_id = book_id
#         self.rating = rating
#         self.feedback = feedback
    
