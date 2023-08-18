import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)

import pandas as pd
import pytest
import requests
from fastapi.testclient import TestClient
from api.api import app
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time

client = TestClient(app)

def test_api_starting():
    """check if the API is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running"}

def test_api_unique_genre():
    """check if the list of unique movies genres is not empty"""
    response = client.get('/unique_genres')
    assert response.status_code == 200
    assert response.json() != None

def test_api_get_random():
    """check if the api gives always a random movie with an user known"""
    response = client.get('/random?user_id=1644')
    assert response.status_code == 200
    assert response.json() != {'message': 'no movie for you:('}

