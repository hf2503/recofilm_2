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
#from api.api import read_root
from fastapi import FastAPI, HTTPException, Response, status, Depends, Header, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time

mock_data = pd.DataFrame([[1,3.5,1644,
                           'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],
                           index=['1'],
                           columns=['movieId','rating','userId','genres','title'])

BASE_URL = 'http://localhost:8000'



#def test_api_starting(requests_mock):
    #requests_mock.get(f'{BASE_URL}/', json= {"message": "API is up and running"})
    #resp = read_root()
    #assert resp == {"message": "API is up and running"}
mock_data = pd.DataFrame([[1,3.5,1644,
                           'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],
                           index=['1'],
                           columns=['movieId','rating','userId','genres','title'])

def test_api_starting(requests_mock):
    requests_mock.get(f'{BASE_URL}/', json= {"message": "API is up and running"})
    assert {"message": "API is up and running"} == requests.get(f'{BASE_URL}/').json()


def test_get_unique_genres(requests_mock):
    all_genres = mock_data['genres'].str.split('|', expand=True).stack().tolist()
    unique_genres = sorted(set(all_genres))
    requests_mock.get(f'{BASE_URL}/unique_genres', json= {"genres": unique_genres })
    assert {"genres": unique_genres} == requests.get(f'{BASE_URL}/unique_genres').json()

def test_get_unique_movies(requests_mock):
    all_movies = mock_data['title'].unique().tolist()
    requests_mock.get(f'{BASE_URL}/unique_movies', json= {"genres":all_movies})
    assert {"genres": all_movies} == requests.get(f'{BASE_URL}/unique_movies').json()

def test_get_random_output(requests_mock):
    all_movies = mock_data['title'].unique().tolist()
    requests_mock.get(f'{BASE_URL}/unique_movies', json= {"genres":all_movies})
    assert {"genres": all_movies} == requests.get(f'{BASE_URL}/unique_movies').json()