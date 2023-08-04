import pytest
import requests
from fastapi.testclient import TestClient
from api import app
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from requests.auth import HTTPBasicAuth


