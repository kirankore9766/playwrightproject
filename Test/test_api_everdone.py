import pytest
import requests


@pytest.mark.skip(reason="Reqres API key required")
def test_create_user():

    url = "https://reqres.in/api/users"

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