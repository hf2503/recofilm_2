import pandas as pd
from pathlib import Path
import pickle
import os
import sys,os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
from utils.utils import make_directory
from model_job.model_utils import *
#from model_job.model.utils import *
from utils.path import input_data_folder, output_folder
from utils.path import *
from preprocessing_job.create_data import Data
print(get_last_final_csv(data_folder))
print(data_folder)
print(os.path.dirname(data_folder))
print(os.path.join((data_folder),'unittest/data_api.pkl'))

print(make_directory(unittest_folder))
print(unittest_folder)
print(os.path.join(unittest_folder,'test_data_final.pkl'))

def get_data_final_pkl():
    file_path = os.path.join(unittest_folder,'test_data_final.pkl')
    with open(file_path,'rb') as df:
        return pickle.load(df)

def get_data_api_pkl():
    file_path = os.path.join(unittest_folder,'test_data_api.pkl')
    with open(file_path,'rb') as df:
        return pickle.load(df)


print(get_data_api_pkl())


def get_last_final_pkl(data_folder):
    pkl_files = [file for file in os.listdir(data_folder) if file.startswith("test") and file.endswith(".pkl")]
    if not pkl_files:
        print("No pkl files starting with 'final' found in the data folder.")
        return None
    pkl_files.sort(key=lambda x: os.path.getctime(os.path.join(data_folder, x)), reverse=True)
    last_final_pkl= pkl_files[0]
    return os.path.join(data_folder, last_final_pkl)

print(get_last_final_pkl(unittest_folder))


def test_existence_final_pkl():
    assert get_last_final_pkl(unittest_folder) != None

def test_existence_data_api_pkl():
    """check if the file data_api.csv exist"""
    csv_files = [file for file in os.listdir(unittest_folder) if file.startswith("test") and file.endswith(".pkl")]
    assert len(csv_files) == 2

def test_shape_final_csv():
    """check if final_*.csv is not empty """
    #data_path = get_last_final_csv(data_folder)
    df = get_data_final_pkl()
    assert df.empty == False

def test_shape_data_api_csv():
    """check if data_api.csv is not empty """
    #csv_files = [file for file in os.listdir(data_folder) if file.startswith("data_api") and file.endswith(".csv")]
    #data_api_path = csv_files[0]
    #df_api = pd.read_csv(data_folder+'/data_api.csv')
    df_api = get_data_api_pkl()
    assert df_api.empty == False

def test_nan_final_csv():
    """ check the Nan of the Dataframe final_*.csv"""
    #data_path = get_last_final_csv(data_folder)
    #df = pd.read_csv(data_path)
    df_data_final = get_data_final_pkl()
    assert df_data_final.isna().sum().all() == False

def test_type_final_csv():
    """check the variable type of the Dataframe final_*csv"""
    #data_path = get_last_final_csv(data_folder)
    df_test_type_final = get_data_final_pkl()
    assert \
        list(df_test_type_final.select_dtypes(include='int64').columns) == ['movieId', 'userId', 'timestamp', 'tagId'] \
        and\
        list(df_test_type_final.select_dtypes(include='float64').columns) == ['rating', 'relevance']\
        #and\
        #list(df.select_dtypes(include='string').columns) == ['title','genres','tag','user_tag']