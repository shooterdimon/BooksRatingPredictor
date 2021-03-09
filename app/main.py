from fastapi import FastAPI
from app.data import Data
from app.functions import *
import pandas as pd
import pickle
import uvicorn

app = FastAPI()

xgb = pickle.load(open(r'app/models/xgb.pickle', 'rb'))


@app.get('/')
async def root():
    return {"message": "Welcome to Book Rating predictor"}


@app.post("/predict", status_code=200)
def predict(data: Data):
    # Extract data in correct order
    df_data = pd.DataFrame(data.dict(),index=[0])
    to_predict = prepare_data(df_data)
    response = xgb.predict(to_predict)
    return {'prediction': float(response[0])}


def prepare_data(df_data):
    df_pages = book_pages(df_data['book_pages'])
    df_image_area = book_image_area(df_data['book_image_url'])
    df_book_review_count = book_review_count(df_data['book_review_count'])
    df_book_genre_count = book_genre_count(df_data['book_genre'])
    df_authors_info = authors_info(df_data['book_authors'])
    return pd.concat([df_pages,df_book_review_count, df_image_area, df_book_genre_count, df_authors_info], axis=1)


# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
