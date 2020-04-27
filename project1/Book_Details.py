import os
from imports import *

def get_book(isbn):
    return db1.session.query(Books).filter(Books.isbn == isbn).all()
def get_book_author(author):
    return db1.session.query(Books).filter(Books.author==author).all()