import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from joblib import dump, load


class MovieModel:

    @staticmethod
    def prepare_data(df: pd.DataFrame):
        df = df[['movieId', 'rating', 'userId']].drop_duplicates()
        rating_matrix = df.pivot(index='movieId', columns='userId', values='rating').fillna(0)
        return csr_matrix(rating_matrix.values)

    def fit(self, df: pd.DataFrame, n_neighbors: int):
        rating_matrix = self.prepare_data(df)
        model = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=n_neighbors)
        model.fit(rating_matrix)
        dump(model, 'movie_model.joblib')

    def predict(self, df: pd.DataFrame, movie_title: str, num_recommendations: int, title_dict: dict):
        model = load('movie_model.joblib')
        movie_id = title_dict[movie_title]
        rating_matrix = self.prepare_data(df)
        distances, indices = model.kneighbors(rating_matrix[movie_id], n_neighbors=num_recommendations)

        # drop the first index being the movie itself
        #indices = np.delete(indices, 0)

        # print titles of those movies
        recommendations = df[['movieId', 'rating', 'userId','title']].drop_duplicates().reset_index(drop=True)['title'][indices[0]].to_list()
        return recommendations

    def evaluate(self,df: pd.DataFrame, movie_title: str, num_recommendations: int, title_dict: dict):
        recommendations = self.predict(df,movie_title,num_recommendations, title_dict)
        user_eval = df[df['title'] == movie_title]['userId'].unique()
        sub_df = df[(df['userId'].isin(user_eval)) & (df['title'].isin(recommendations))][['movieId', 'rating', 'userId','title']].drop_duplicates()
        score = sub_df.groupby('title').agg({'rating': 'mean', 'userId': 'count'})
        print(score)

    def stability(self,df: pd.DataFrame, movie_title: str, num_recommendations: int, title_dict: dict):
        i = 0
        recommendations = []
        while i <10:
            rec = self.predict(df,movie_title,num_recommendations, title_dict)
            recommendations.extend(rec)
            i+=1
        arr, count = np.unique(recommendations, return_counts=True)
        count = count/10
        dict_stability = {k:v for k,v in zip(arr, count)}
        print(dict_stability)

    def prediction_comparaison(self,df: pd.DataFrame, movie_title: list[str], num_recommendations: int, title_dict: dict):
        i = 0
        recommendations = []
        for m in movie_title:
            rec = self.predict(df,m,num_recommendations, title_dict)
            recommendations.extend(rec)
            i+=1
        arr, count = np.unique(recommendations, return_counts=True)
        count = count/len(movie_title)
        dict_stability = {k:v for k,v in zip(arr, count)}
        print(dict_stability)


