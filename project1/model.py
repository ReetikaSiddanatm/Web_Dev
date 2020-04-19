from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class Registartion(db.Model):
    __tablename__ = "Registartion"
    Firstname = db.Column(db.String, primary_key=True)
    Email = db.Column(db.String, nullable=False)
    datetime = db.Column(db.String,nullable= False)
    
