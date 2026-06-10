import requests


def test_create_user():

    url = "https://reqres.in/api/users"   # Sample API for testing

    payload = {
        "name": "Kiran",
        "job": "QA Engineer"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(
        url,
        json=payload,
        headers=headers
    )

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201