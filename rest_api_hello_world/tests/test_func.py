import json

import requests

URL_GET_DATA = 'http://0.0.0.0:8080/data'
URL_HELLO_WORLD = "http://0.0.0.0:8080/hello_world"


def test_get_hello_world_ok():
    response = requests.get(URL_HELLO_WORLD)

    assert response.ok


def test_get_hello_world_text():
    response = requests.get(URL_HELLO_WORLD)

    text = json.loads(response.text)

    assert text["text"].lower() == "hello world"


def test_get_hello_world_bad_request():
    response = requests.get("http://0.0.0.0:8080/world")

    assert (response.status_code >= 400 and
            response.status_code < 500)


def test_post_data_ok():
    response = requests.post(URL_GET_DATA)

    assert response.ok


def test_post_data_get_json():
    response = requests.post(url=URL_GET_DATA,
                             headers={'Content-Type': 'application/json'},
                             data='{"data":"hello_world 2"}')

    text = json.loads(response.text)

    assert text is not None
