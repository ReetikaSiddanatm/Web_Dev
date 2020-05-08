import os
import logging
import json
import requests



# if not os.getenv("DATABASE_URL"):
#     raise RuntimeError("DATABASE_URL is not set")

# engine = create_engine(os.getenv("DATABASE_URL"))
# db_session = scoped_session(sessionmaker(bind=engine))
def get_bookreads_api(isbn):
    query = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": 'lvf1KDsIp4YNCOOMqOZWg' , "isbns": isbn})
    logging.debug("goodreads call success")
    response = query.json()
   
    return response