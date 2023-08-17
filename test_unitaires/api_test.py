import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)

import pytest
import requests
from fastapi.testclient import TestClient
from api.api import app
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time
#from api_utils.utils import *


#data, movie_data, user_data, title_dict = get_data()

#client = TestClient(app)

def test_api_starting():
    """check if the API is running."""
    url = 'http://localhost:8000'
    response = requests.get(url)

    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running"}

#print(data)


