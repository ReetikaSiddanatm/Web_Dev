import requests
res = requests.get("https://www.goodreads.com/book/review_counts.json", params={"key": " lvf1KDsIp4YNCOOMqOZWg", "isbns": "9781632168146"})
print(res.json())

{'books': [{
                'id': 29207858,
                'isbn': '1632168146',
                'isbn13': '9781632168146',
                'ratings_count': 0,
                'reviews_count': 1,
                'text_reviews_count': 0,
                'work_ratings_count': 26,
                'work_reviews_count': 113,
                'work_text_reviews_count': 10,
                'average_rating': '4.04'
            }]
}