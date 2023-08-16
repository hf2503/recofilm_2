import sys
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)

print(sys.path)
import pytest
import requests
from fastapi.testclient import TestClient
from api.api import app
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time

client = TestClient(app)

def test_api_starting():
    """Test if the API is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running"}

def test_bestMoviesBygenre_2():
    response = client.get("/bestMoviesByGenre",
                          params={"genre": "Adventure"},
                          headers={"Authorization": "Basic MTY0NDo="})
    assert response.status_code == 200
    assert response.json() == ["Toy Story (1995) (id = 1)"]

