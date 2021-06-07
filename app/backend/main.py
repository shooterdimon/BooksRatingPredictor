from fastapi import FastAPI
from data import DataAPI,DataFront
from functions import *
import pandas as pd
import pickle
import uvicorn
import xgboost

app = FastAPI(title="Rate your book",
              description="Rating predictor service built on goodread`s dataset",
              version="1.0")

xgb = pickle.load(open(r'models/xgb.pickle', 'rb'))


@app.get('/')
async def root():
    return {"message": "Welcome to Book Rating predictor"}


@app.post("/predict-api", status_code=200)
def predict_api(data: DataAPI):
    # Extract data in correct order
    df_data = pd.DataFrame(data.dict(),index=[0])
    to_predict = prepare_data_api(df_data)
    response = xgb.predict(to_predict)
    return {'prediction': float(response[0])}


@app.post("/predict-front", status_code=200)
def predict_front(data: DataFront):
    # Extract data in correct order
    df_data = pd.DataFrame(data.dict(),index=[0])
    to_predict = prepare_data_front(df_data)
    response = xgb.predict(to_predict)
    return {'prediction': float(response[0])}



def prepare_data_api(df_data):
    df_pages = book_pages(df_data['book_pages'])
    df_image_area = book_image_area(df_data['book_image_url'])
    df_book_review_count = book_review_count(df_data['book_review_count'])
    df_book_genre_count = book_genre_count(df_data['book_genre'])
    df_authors_info = authors_info(df_data['book_authors'])
    return pd.concat([df_pages,df_book_review_count, df_image_area, df_book_genre_count, df_authors_info], axis=1)


def prepare_data_front(df_data):
    df_pages = df_data['book_pages']
    df_image_area = pd.DataFrame({'book_image_area':df_data['book_image_url']},index=[0])
    df_book_review_count = book_review_count(df_data['book_review_count'])
    df_book_genre_count = book_genre_count(df_data['book_genre'])
    df_authors_info = authors_info(df_data['book_authors'])
    return pd.concat([df_pages,df_book_review_count, df_image_area, df_book_genre_count, df_authors_info], axis=1)



def save_image(image,img_path):
    with open(img_path,'wb') as file:
        file.write(image)

# if __name__ == '__main__':
#     uvicorn.run(app, host='127.0.0.1', port=8000)
