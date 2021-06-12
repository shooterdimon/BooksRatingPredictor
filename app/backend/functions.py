import pandas as pd
import numpy as np
from skimage import io
from objects import *


def book_pages(s):
    return pd.DataFrame(s.str.extract(r'(\d+)'), columns=['book_pages']).fillna(value=0).astype('int')


def book_image_area(s):
    arr = []

    for url in s.values:
        try:
            height, width = io.imread(url).shape[:2]
            arr.append(height * width)
        except Exception:
            arr.append(0)

    return pd.DataFrame({'book_image_area': arr})


def book_review_count(s):
    return pd.DataFrame(s.fillna(value=0))


def book_genre_count(s):
    top_genres = genres_data.sort_values(by='count', ascending=False)['genre'].head(30).values
    return pd.DataFrame(s.map(lambda x: sum([1 for genre in np.unique(x.split('|')) if genre in top_genres])
                              if pd.notna(x) else 0)).rename(columns={s.name: 'book_genre_count'})


def authors_info(s):
    info_arr = []
    for authors in s.map(lambda x: np.unique(x.split('|'))).values:
        arr = []
        for author in authors:
            if author in authors_dict:
                arr.append(list(authors_dict[author].values()))
        info_arr.append(
            np.array(arr if len(arr) else [np.nan] * 3).mean(axis=0).flatten() if len(arr) else [np.nan] * 3)
    return pd.DataFrame(info_arr, columns=['author_work_count', 'author_average_rating', 'author_review_count']) \
        .fillna(value={'author_work_count': 0, 'author_average_rating': 0, 'author_review_count': 0})
