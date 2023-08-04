from preprocessing.create_data_3 import Data
from model.movie_model import MovieModel
from model.utils import split_data_random, check_overlap

TEST_SIZE = 0.3

df = Data().data
print(df.columns)
train, test, title_dict = split_data_random(df)
print(train.shape)
print(test.shape)
check_overlap(train, test)
model_movie= MovieModel()
model_movie.fit(df, 10)
title = 'Star Wars: Episode IV - A New Hope (1977)'
print(title_dict.get(title))
print(df[df['title'] == 'Star Wars: Episode IV - A New Hope (1977)'])
recommendations= model_movie.evaluate(df, title, 10, title_dict)
recommendations_2 = model_movie.predict(df,title,10,title_dict)
model_movie.stability(df, title, 10, title_dict)
model_movie.prediction_comparaison(df, ['Star Wars: Episode IV - A New Hope (1977)', 'Junior (1994)', 'Interview with the Vampire: The Vampire Chronicles (1994)'], 10, title_dict)
print(recommendations_2)