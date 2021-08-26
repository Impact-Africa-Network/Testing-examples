# We will use https://reqres.in/


import pytest
import requests
import json

main_url = 'https://reqres.in/'

@pytest.mark.login
def test_login_success():
    login_url = main_url + 'api/login'

    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(login_url, data)

    assert response.status_code == 200

    token = json.loads(response.text)

    assert token['token'] == 'QpwL5tke4Pnpja7X4'








