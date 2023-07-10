import pytest
import json
import string
import random

from api import app

def test_valid_request():
    test_json_obj = {"age": 38, "name": "Yuval Yaari"};
    response = app.test_client().post('/users', json=test_json_obj)

    assert response.status_code == 201
    # Verify that the returned JSON equals the JSON we posted
    assert json.dumps(json.loads(response.data.decode('utf-8')), sort_keys=True) == json.dumps(test_json_obj, sort_keys=True)

def test_invalid_request():
    test_json_obj = {"age": 38, "name": "Yuval Yaari"};
    # Send the object as form data, not JSON
    response = app.test_client().post('/users', data=test_json_obj)

    assert response.status_code == 400

def test_invalid_name():
    # Generate a name of 33 characters
    long_name = ''.join(random.choices(string.ascii_letters, k=33))
    test_json_obj = {"age": 38, "name": long_name};
    response = app.test_client().post('/users', json=test_json_obj)

    assert response.status_code == 400

def test_invalid_age_not_number():
    test_json_obj = {"age": "38", "name": "Yuval Yaari"};
    response = app.test_client().post('/users', json=test_json_obj)

    assert response.status_code == 400

def test_invalid_age_less_than_16():
    test_json_obj = {"age": 13, "name": "Yuval Yaari"};
    response = app.test_client().post('/users', json=test_json_obj)

    assert response.status_code == 400
