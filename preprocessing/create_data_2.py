import pandas as pd
import os
import gc

class Data:
    def __init__(self):
        data = self.load_data()
        self.merged_path = '../ml-20m/merged.csv'
        self.final_path = '../ml-20m_final/data_final_2.csv'

    def load_data(self):
        if os.path.exists(self.final_path):
            return pd.read_csv(self.final_path)
        else:
            return self.prepare_data()
    
    def create_data(self):
        movie_df = pd.read_csv('../ml-20m/movies.csv')
        ratings_df = pd.read_csv('../ml-20m/ratings.csv')
        gen_tag_df = pd.read_csv('../ml-20m/genome-tags.csv')
        scores_df = pd.read_csv('../genome-scores.csv')
        links_df = pd.read_csv('../ml-20m\links.csv')
        tags_df = pd.read_csv('../ml-20m\tags.csv')
        movies_tag = tags_df.merge(movie_df,on =['movieId'], how='left')
        df_movtag_rat = movies_tag.merge(ratings_df, on= ['movieId','userId'],how = 'inner')
        df_movtag_rat = df_movtag_rat.drop('genres',axis=1).join(df_movtag_rat['genres'].str.get_dummies('|'))
        df_movtag_rat.to_csv(self.merged_path,index=False)
        return df_movtag_rat
    
    def prepare_data(self):
        if os.path.exists(self.merged_path):
            df = pd.read_csv(self.merged_path)
        else:
            df = self.create_data()
            df['year'] = df['title'].str.extract(r'([0-9]{4})')
            #df['title'] = df['title'].str.extract(r'([0-9]{4})')
        df.to_csv(self.final_path,index=False)
        return df