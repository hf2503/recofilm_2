import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
from unittest.mock import MagicMock, call, mock_open, patch
import pandas as pd
import pytest
import requests
from fastapi.testclient import TestClient
from api.api import *
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time



mock_data = pd.DataFrame([[1,3.5,1644,'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],index=['1'],columns=['movieId','rating','userId','genres','title'])

def test_unique_genres():
    with patch('api.api.data', mock_data):
        result = unique_genres()

    expected_result = {
        'genres': ['Action', 'Adventure', 'Comedy', 'Drama', 'Romance', 'War']
    }
    
    assert result == expected_result