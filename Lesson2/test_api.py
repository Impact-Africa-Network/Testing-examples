# In this scenario we will test login using an external api
# We will use https://reqres.in/


import pytest
import requests
import json


main_url = "https://reqres.in/"

def test_valid_login():
    login_url = main_url + 'api/login'
    data = {
        "email" : "kefa@impactafrica.network",
        "password" : "abc"
    }
    response = requests.post(login_url, data)

    token = json.loads(response.text)
    assert response.status_code == 200
    assert token['token'] == 'QpwL5tke4Pnpja7X4'


