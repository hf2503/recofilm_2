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
from api.api import read_root
from fastapi import FastAPI, HTTPException, Response, status, Depends, Header, Query
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth
import time

mock_data = pd.DataFrame([[1,3.5,1644,
                           'Adventure|Animation|Children|Comedy|Fantasy','Toy Story (1995)']],
                           index=['1'],
                           columns=['movieId','rating','userId','genres','title'])

BASE_URL = 'http://localhost:8000'



def test_api_starting(requests_mock):
    requests_mock.get(f'{BASE_URL}/', json= {"message": "API is up and running"})
    resp = read_root()
    assert resp == {"message": "API is up and running"}

