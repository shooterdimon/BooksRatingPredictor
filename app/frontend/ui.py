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
cover = book_image_container.file_uploader(label='Choose image', help='Book cover importance is 1.7%')
if cover:
    book_image_container.image(cover.getvalue())
    height, width = imageio.imread(cover.getvalue()).shape[:2]
    request_json['book_image_url'] = height*width
else:
    request_json['book_image_url'] = 0


# book_genre
book_genre_container = st.beta_container()
book_genre_container.subheader('Select genres')
genres_select = book_genre_container.multiselect(label="Genres",options=genres, help='Book genre importance is 2,4%.\nYou can select as many genres as you can')
if genres_select:
    request_json['book_genre']= "|".join(genres_select)
else:
    request_json['book_genre']= 0


# book_authors
book_authors_container = st.beta_container()
book_authors_container.subheader("Type authors' names")
authors_select = book_authors_container.text_input(label="Authors", help='Author importance is about 90.5%. Our predictor based on GoodReads dataset, '
                                                                         'that means other authors get bad prediction, because we do not have enough information.')
if authors_select:
    request_json['book_authors']= "|".join(authors_select.split(','))
else:
    request_json['book_authors']= 0


# book_page
book_page_container = st.beta_container()
book_page_container.subheader('Choose number of pages from slider')
pages_slider = book_page_container.slider(label="Pages",min_value=0,max_value=14000,step=50, help='Book pages importance is 2,6%')
if pages_slider:
    request_json['book_pages']= pages_slider
else:
    request_json['book_pages']= 0


# book_review_count
book_review_container = st.beta_container()
book_review_container.subheader('Write number of reviews')
review_input = book_review_container.number_input(label='Reviews',min_value=0, help='Book reviews importance is 2.8%')
if review_input:
    request_json['book_review_count']= review_input
else:
    request_json['book_review_count']= 0



def make_predict(url, features):
    response = requests.post(url, json=features)
    return round(response.json()['prediction'],2)

if st.button(label='Make Predict'):
    predict = make_predict(backend+ep_predict, request_json)

    if request_json['book_image_url']==0:
        book_image_container.warning('You did not upload image. To make more accurate prediction, please upload book cover')
    elif request_json['book_genre'] == 0:
        book_genre_container.warning(
            'You did not specify genres. To make more accurate prediction, please choose at least one')

    elif request_json['book_authors'] == 0:
        book_authors_container.warning(
            'You pass author field empty. To make more accurate prediction, please write at least one')

    elif request_json['book_pages'] == 0:
        book_page_container.warning(
            'You did not specify number of pages. To make more accurate prediction, please select from slider')

    elif request_json['book_review_count'] == 0:
        book_review_container.warning(
            'You did not write number of book`s reviews. To make more accurate prediction, please write a number')

    st.success(f'Predicted rating is in range {round(predict-0.18,2)}-{round(predict+0.18,2)}')
    st.balloons()