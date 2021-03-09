import requests
import pandas as pd

df_request = pd.read_csv(r"../notebooks/data/train.csv")
url_heroku = 'https://get-book-rating.herokuapp.com/predict'
url_local = 'http://127.0.0.1:8000/predict'

for i in range(10):
    to_predict_json = {"book_title": df_request["book_title"][i],
                   "book_image_url": df_request["book_image_url"][i],
                   "book_desc": df_request["book_desc"][i],
                   "book_genre": df_request["book_genre"][i],
                   "book_authors": df_request["book_authors"][i],
                   "book_format": df_request["book_format"][i],
                   "book_pages": df_request["book_pages"][i],
                   "book_review_count": int(df_request["book_review_count"][i]),
                   "book_rating_count": int(df_request["book_rating_count"][i])}
    r = requests.post(url_heroku, json=to_predict_json)
    print(r.json())













# to_predict_dict = {"book_title": "Writing about Magic",
#                   "book_image_url": "https",
#                   "book_desc": "Do you write fantasy fiction? This book is a resource for authors. Crammed with information, tips, a....",
#                   "book_genre": "Language|Writing|Nonfiction",
#                   "book_authors": "Rayne Hall",
#                   "book_format": "Paperbook",
#                   "book_pages": "180 pages",
#                   "book_review_count": 27,
#                   "book_rating_count": 126}

#r = requests.post(url,json=to_predict_dict)
#print(r.json())
