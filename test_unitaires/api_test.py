import sys
import os

#ajout pour lire les fichiers
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
sys.path.append('../api')
#fin ajout

from unittest.mock import MagicMock, call, mock_open, patch
import pandas as pd
import pytest
import requests
from fastapi.testclient import TestClient
from api.api import read_root,unique_genres,unique_movies,random_output,movie_model,user_model
from api.api_utils.utils import query_params
from fastapi import FastAPI, HTTPException, Response, status, Depends, Header, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time

mock_data = pd.DataFrame([[1,3.5,1644,
                           'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],
                           index=['1'],
                           columns=['movieId','rating','userId','genres','title'])

BASE_URL = 'http://localhost:8000'

mock_data = pd.DataFrame([[1,3.5,1644,
                           'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],
                           index=['1'],
                           columns=['movieId','rating','userId','genres','title'])

def test_api_starting(requests_mock):
    requests_mock.get(f'{BASE_URL}/', json= {"message": "API is up and running"})
    assert read_root() == requests.get(f'{BASE_URL}/').json()


def test_get_unique_genres(requests_mock):
    with patch('api.api.data',mock_data):
        result = unique_genres()
    requests_mock.get(f'{BASE_URL}/unique_genres', json= {"genres": ["Adventure","Animation","Children",
                                                                     "Comedy","Fantasy",]})
    assert result == requests.get(f'{BASE_URL}/unique_genres').json()

def test_get_unique_movies(requests_mock):

    requests_mock.get(f'{BASE_URL}/unique_movies', json= {"movies":['Toy Story (1995)']})
    with patch('api.api.data',mock_data):
        result = unique_movies()
    assert result == requests.get(f'{BASE_URL}/unique_movies').json()

def test_get_random_output(requests_mock):
    requests_mock.get(f'{BASE_URL}/random?user_id=1644',json= {'message': 'No movie for you :('})
    with patch('api.api.data',mock_data):
        result = random_output(query_params = {'user_id':'1644','subject':'','movie_name':''})
    assert result == requests.get(f'{BASE_URL}/random?user_id=1644').json()

def test_get_movie_model(requests_mock):
    requests_mock.get(f'{BASE_URL}/movie_model?user_id=1644&movie_name=Toy%20Story%20%281995%294',json= {'message': 'No movie for you :('})
    with patch('api.api.data',mock_data):
        result = movie_model(query_params = {'user_id':'1644','subject':'','movie_name':'Toy Story (1995)'})
        assert result == requests.get(f'{BASE_URL}/movie_model?user_id=1644&movie_name=Toy%20Story%20%281995%294').json()

def test_get_user_model(requests_mock):
    requests_mock.get(f'{BASE_URL}/user_model?user_id=1644',json= {'message': 'No movie for you :('})
    with patch('api.api.data',mock_data):
        result = user_model(query_params = {'user_id':'1644','subject':'','movie_name':'Toy Story (1995)'})
        assert result == requests.get(f'{BASE_URL}/user_model?user_id=1644').json()

#def test_get_user_model(request_mock)
