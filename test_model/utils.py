import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from joblib import dump, load


def check_overlap(train_data, test_data):
    train_data = train_data[['movieId', 'userId']].drop_duplicates()
    test_data = test_data[['movieId', 'userId']].drop_duplicates()
    overlap = pd.merge(train_data[['movieId', 'userId']], test_data[['movieId', 'userId']], on=['movieId', 'userId'],
                       how='inner')

    # Vérifier si overlap est vide
    if overlap.empty:
        print("Aucune combinaison 'movieId', 'userId' n'est présente dans les deux ensembles.")
    else:
        print(
            "Certaines combinaisons 'movieId', 'userId' sont présentes à la fois dans les ensembles de train et de test.")
        print(overlap)

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

def split_data_random(df: pd.DataFrame):
    unique_combinations = df[['movieId', 'userId']].drop_duplicates()

    # Mélanger les combinaisons uniques
    shuffled_combinations = unique_combinations.sample(frac=1, random_state=42)

    # Calculer la taille de l'ensemble de test
    test_size = int(0.2 * len(shuffled_combinations))

    # Diviser les combinaisons en ensembles de train et de test
    test_combinations = shuffled_combinations.iloc[:test_size]
    train_combinations = shuffled_combinations.iloc[test_size:]

    # Diviser les données en fonction des combinaisons de train et de test
    train_data = df.merge(train_combinations, on=['movieId', 'userId'], how='inner')
    test_data = df.merge(test_combinations, on=['movieId', 'userId'], how='inner')

    temp = train_data[['title', 'movieId']].drop_duplicates()
    title_dict = pd.Series(temp.movieId.values, index=temp.title).to_dict()
    return train_data, test_data, title_dict

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