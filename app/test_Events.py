import requests

# URL waar de API op draait
APP_URL = "http://127.0.0.1:8000"


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
