import requests

# URL waar de API op draait
APP_URL = "http://127.0.0.1:8000"



# Test gebruiker aanmaken
def test_create_test_user():
    credentials = {
        "email": "example@contoso.com",
        "password": "test"
    }
    response = requests.post(f"{APP_URL}/users/", json=credentials)
    assert response.status_code == 200
    user = response.json()
    assert user["email"] == credentials["email"]


#Get auth token
def get_auth_token(username: str, password: str):
    token_data = {
        "username": "example@contoso.com",
        "password": "test",
        "grant_type": "password",
        "scope": "openid",
        "client_id": "",
        "client_secret": "",
    }
    response = requests.get(f"{APP_URL}/token", data=token_data)
    return response.json().get("access_token")

# Test alle POST endpoints
def test_create_event():
    event_data = {
        "name": "Test event",
        "city": "Hasselt",
        "startdate": "2021-01-02",
        "enddate": "2021-01-04",
        "isPaid": True,
    }

    response = requests.post(f"{APP_URL}/events/", json=event_data)
    assert response.status_code == 401 # 401 = Unauthorized niet ingelogd
    login_token = get_auth_token("example@contoso.com", "test")
    response = requests.post(f"{APP_URL}/events/", json=event_data, headers={"Authorization": f"Bearer {login_token}"})

    created_event = response.json()
    assert created_event["name"] == event_data["name"]
    assert created_event["city"] == event_data["city"]
    assert created_event["startdate"] == event_data["startdate"]
    assert created_event["enddate"] == event_data["enddate"]
    assert created_event["isPaid"] == event_data["isPaid"]

# Test alle GET endpoints

# GET all events: /events/
def test_get_all_events():
    response = requests.get(f"{APP_URL}/events/")
    assert response.status_code == 200

# GET event by id: /events/id/{event_id}
def test_get_event_by_id():
    response = requests.get(f"{APP_URL}/events/id/1")
    assert response.status_code == 200

# GET all events in city: /events/city/{city}
def test_get_events_by_city():
    response = requests.get(f"{APP_URL}/events/city/Hasselt")
    assert response.status_code == 200


# Test alle PUT endpoints
def test_update_event():
    event_data = {
        "name": "Test event",
        "city": "Genk",
        "startdate": "2021-01-02",
        "enddate": "2021-01-04",
        "isPaid": True,
    }

    response = requests.put(f"{APP_URL}/events/id/1", json=event_data)
    assert response.status_code == 401 # 401 = Unauthorized niet ingelogd
    login_token = get_auth_token("example@contoso.com", "test")
    response = requests.put(f"{APP_URL}/events/id/1", json=event_data, headers={"Authorization": f"Bearer {login_token}"})

    updated_event = response.json()
    assert updated_event["name"] == event_data["name"]
    assert updated_event["city"] == event_data["city"]
    assert updated_event["startdate"] == event_data["startdate"]
    assert updated_event["enddate"] == event_data["enddate"]
    assert updated_event["isPaid"] == event_data["isPaid"]

# Test alle DELETE endpoints
def test_delete_event():
    response = requests.delete(f"{APP_URL}/events/1")
    assert response.status_code == 401 # 401 = Unauthorized niet ingelogd
    login_token = get_auth_token("example@contoso.com", "test")
    response = requests.delete(f"{APP_URL}/events/1", headers={"Authorization": f"Bearer {login_token}"})
    assert response.status_code == 200 # 200 = OK
    assert response.json() == {"message": "Event deleted successfully"}






