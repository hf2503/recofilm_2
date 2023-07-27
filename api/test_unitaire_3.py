import pytest
import requests
from fastapi.testclient import TestClient
from api import app
import sys
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth

client = TestClient(app)


def test_api_starting():
    """teste le fonctionnement de l'API"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message":"API is up and running"}




def test_bestMoviesBygenre_2():
    url="http://127.0.0.1:8000/bestMoviesByGenre?genre=Adventure"
    basic = HTTPBasicAuth('1644','')
    response = requests.get(url,auth=basic)
    assert response.status_code == 200
    assert response.json() == ["Toy Story (1995) (id = 1)"]

#def test_bestMoviesBygenre():
    #basic = HTTPBasicCredentials('1644','')
    #response = client.get("/bestMoviesByGenre",auth=basic)#auth=HTTPBasicCredentials('1644'))
    #assert response.status_code == 200
    #print(response.status_code)
    #print(response.json())
    #assert response.json() == ["Toy Story (1995) (id = 1)"]

