import pandas as pd
import sys
sys.path.append('../preprocessing')
sys.path.append('ml-20m')
import os

from utils import *
from create_data import Data


def test_check_overlap():
    df=Data(min_relevance=0.85,min_rating=4000).data
    train_data, test_data, title_dict = split_data_random(df)
    assert check_overlap(train_data,test_data) == True


#test_check_overlap()

print("ok")
print(sys.path)
print(os.path.dirname(os.path.abspath(__file__)))
