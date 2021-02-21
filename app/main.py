from fastapi import FastAPI
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBRegressor
from data import Data
import numpy as np
import uvicorn
import pickle
import os



app = FastAPI()


clf = pickle.load(open('models/model.pickle', 'rb'))
vectorizer = pickle.load(open('models/tf_idf.pickle', 'rb'))
features_names = ['book_pages','book_rating_count']



@app.get('/')
async def root():
    return {"message" : "Hello world!"}


@app.post("/predict",status_code=200)
def predict(data: Data):
    # Extract data in correct order
    data_dict = data.dict()
    book_desc = prepare_desc([data_dict['book_desc']])
    data_dict['book_pages'] = prepare_pages(data_dict['book_pages'])
    to_predict = np.concatenate([book_desc,[[data_dict[feature] for feature in features_names]]],axis=1)
    response = clf.predict(to_predict)
    return {'prediction':float(response[0])}




def prepare_desc(desc):
    return vectorizer.transform(desc).toarray()

def prepare_pages(pages):
    return float(pages.split(" ")[0])


if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)