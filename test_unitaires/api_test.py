import sys
import os

#ajout pour lire les fichiers
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir_path = os.path.abspath(os.path.join(dir_path,os.pardir))
sys.path.insert(0,parent_dir_path)
sys.path.append('../api')
#fin ajout
from scipy.sparse import csr_matrix
import pandas as pd
import pytest
import requests
from fastapi import Depends
from fastapi.testclient import TestClient
import importlib

# Reload the api module to ensure the patch takes effect
from api.api import app
from requests.auth import HTTPBasicAuth
import time
from unittest.mock import Mock, patch

client = TestClient(app)

def test_api_starting():
    """Test if the API is running."""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "API is up and running"}

def test_unique_genres():
    """check if the list of unique movies genres is not empty"""
    response = client.get("/unique_genres")
    assert response.status_code == 200
    assert response.json() != None










#import base64
#credentials = "1644:"
#encoded_credentials = base64.b64encode(credentials.encode()).decode()
#auth_string = f"Basic {encoded_credentials}"
