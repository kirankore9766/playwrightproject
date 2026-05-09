import requests

#def test_get_user():
 #   response = requests.get("https://app.everdone.ai/login")
  #  assert response.status_code == 200

 

# def test_get_user():
#     response = requests.get("https://app.everdone.ai/login")
#     assert response.status_code == 200


def test_create_user():

    payload = {
        "name": "Kiran",
        "job": "QA Engineer"
    }

    response = requests.post(
        "https://app.everdone.ai/login",
        json=payload
    )

    print(response.status_code)
    print(response.text)

    assert response.status_code in [200, 201, 400]