import numpy as np
import pandas as pd




def stability(self,df: pd.DataFrame, movie_title: str, num_recommendations: int, title_dict: dict):
    i = 0
    recommendations = []
    while i <100:
        rec = self.predict(df,movie_title,num_recommendations, title_dict)
        recommendations.extend(rec)
        i+=1
    arr, count = np.unique(recommendations, return_counts=True)
    count = count/100
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