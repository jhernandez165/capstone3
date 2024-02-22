import pytest
import requests_mock
from application_data_producer import generate_application_data, submit_application

# Configuration for your test
BASE_URL = 'http://localhost:8071'
APPLICATION_ENDPOINT = f"{BASE_URL}/applications"
HEADERS = {'Authorization': 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbmlzdHJhdG9yIiwiYXV0aG9yaXR5IjoiYWRtaW5pc3RyYXRvciIsImlhdCI6MTcwNzY5NTYyNSwiZXhwIjoxNzA4OTA1MjI1fQ.ebVLchXN7ixbo5BXBGMzNvhCXhRqKj3F9RvlE6MrbnY'}

@pytest.fixture
def application_data():
    """Fixture to generate application data."""
    return generate_application_data()

def test_submit_application_success(requests_mock, application_data):
    """Test submitting an application successfully."""
    mock_response = {
        "status": "APPROVED",
    }
    requests_mock.post(APPLICATION_ENDPOINT, json=mock_response, status_code=201)

    response = submit_application(application_data)
    assert response is True

def test_submit_application_failure(requests_mock, application_data):
    """Test failing to submit an application."""
    requests_mock.post(APPLICATION_ENDPOINT, status_code=400)

    response = submit_application(application_data)
    assert response is False


