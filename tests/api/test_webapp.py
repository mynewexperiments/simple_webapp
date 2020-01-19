import json
import pytest

from src.dev.app import app

@pytest.fixture
def client(request):
    test_client = app.test_client()

    def teardown():
        pass

    request.addfinalizer(teardown)
    return test_client

def post_json(client, url, json_dict):
    return client.post(url, data=json.dumps(json_dict), content_type='application/json')

def json_of_response(response):
    return json.loads(response.data.decode('utf8'))

def test_dummy(client):
    response = client.get('/')
    assert b'hello world' in response.data


