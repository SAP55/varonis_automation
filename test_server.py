import requests

API_SERVER_URL = "http://localhost:8000"
API_USERNAME = "test"
API_PASS = "1234"
API_PASS_WRONG = "12345"

access_token = None
poly_data_id = None


def test_negative_authorize():
    global access_token
    response = requests.post(API_SERVER_URL + '/api/auth', json={
        'username': API_USERNAME,
        'password': API_PASS_WRONG
    })

    assert response.status_code != 200


def test_authorize():
    global access_token
    response = requests.post(API_SERVER_URL + '/api/auth', json={
        'username': API_USERNAME,
        'password': API_PASS
    })

    assert response.status_code == 200

    access_token = response.json().get("access_token")


def test_list_poly_data():
    response = requests.get(API_SERVER_URL + '/api/poly',
                            headers={"Authorization": "Bearer " + access_token, "Content-Type": "application/json"})

    assert response.status_code == 200


def test_post_poly_data():
    global poly_data_id

    response = requests.post(API_SERVER_URL + '/api/poly',
                             headers={"Authorization": "Bearer " + access_token, "Content-Type": "application/json"},
                             json={"data": [{"key": "test_key", "val": "test_value", "valType": "str"}]})

    poly_data_id = response.json().get('id')

    assert response.status_code == 200


def test_get_poly_data():
    response = requests.get(API_SERVER_URL + '/api/poly/' + str(poly_data_id),
                            headers={"Authorization": "Bearer " + access_token, "Content-Type": "application/json"})

    assert response.status_code == 200
    data = response.json().get('data')[0]

    assert data.get('key') == 'test_key'
    assert data.get('val') == 'test_value'


def test_delete_poly_data():
    response = requests.delete(API_SERVER_URL + '/api/poly/' + str(poly_data_id),
                               headers={"Authorization": "Bearer " + access_token, "Content-Type": "application/json"})

    assert response.status_code == 200

    response = requests.get(API_SERVER_URL + '/api/poly/' + str(poly_data_id),
                            headers={"Authorization": "Bearer " + access_token, "Content-Type": "application/json"})

    assert response.status_code != 200
