from preprocessing.create_data_2 import Data
from model.movie_model import MovieModel
from model.utils import split_data_random, check_overlap

TEST_SIZE = 0.3

df = Data().data
print(df['title'])
train, test, title_dict = split_data_random(df)
check_overlap(train, test)
print(df.head)
model_movie= MovieModel()
model_movie.fit(df, 10)
title = 'Star Wars: Episode IV - A New Hope (1977)'
recommendations = MovieModel().evaluate(df, title, 10, title_dict)
model_movie.stability(df, title, 10, title_dict)
model_movie.prediction_comparaison(df, ['Star Wars: Episode IV - A New Hope (1977)', 'Junior (1994)', 'Interview with the Vampire: The Vampire Chronicles (1994)'], 10, title_dict)
print(recommendations)
