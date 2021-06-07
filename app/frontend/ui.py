import streamlit as st
import requests
import imageio
from multiselect_options import genres


backend = 'http://backend:8000'
ep_predict = '/predict-front'
request_json = {}


st.title("Get book rating")
st.header("Book's rating predictor built on goodread's dataset")


#book_image
book_image_container = st.beta_container()
book_image_container.subheader('Upload cover')
cover = book_image_container.file_uploader(label='Choose image')
if cover:
    book_image_container.image(cover.getvalue())
    height, width = imageio.imread(cover.getvalue()).shape[:2]
    request_json['book_image_url'] = height*width
else:
    request_json['book_image_url'] = None


# book_genre
book_genre_container = st.beta_container()
book_genre_container.subheader('Select genres')
genres_select = book_genre_container.multiselect(label="Genres",options=genres)
if genres_select:
    request_json['book_genre']= "|".join(genres_select)
else:
    request_json['book_genre']= None


# book_authors
book_authors_container = st.beta_container()
book_authors_container.subheader("Type authors' names")
authors_select = book_authors_container.text_input(label="Authors")
if authors_select:
    request_json['book_authors']= "|".join(authors_select.split(','))
else:
    request_json['book_authors']= None



# book_page
book_page_container = st.beta_container()
book_page_container.subheader('Choose number of pages from slider')
pages_slider = book_page_container.slider(label="Pages",min_value=0,max_value=14000,step=50)
if pages_slider:
    request_json['book_pages']= pages_slider
else:
    request_json['book_pages']= 0


# book_review_count
book_review_container = st.beta_container()
book_review_container.subheader('Write number of reviews')
review_input = book_review_container.number_input(label='Reviews',min_value=0)
if review_input:
    request_json['book_review_count']= review_input
else:
    request_json['book_review_count']= 0




def make_predict(url, features):
    response = requests.post(url, json=features)
    return round(response.json()['prediction'],2)

if st.button(label='Make Predict'):
    predict = make_predict(backend+ep_predict, request_json)
    st.write(f'Predicted rating is {predict}')
    st.balloons()