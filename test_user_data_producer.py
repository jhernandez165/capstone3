import pytest
import requests_mock
from user_data_producer import create_admin_user 

BASE_URL = 'http://localhost:8070'
REGISTRATION_ENDPOINT = f"{BASE_URL}/users/registration"

@pytest.fixture
def mock_response_success():
    return {"message": "Admin user registered successfully."}

@pytest.fixture
def mock_response_failure():
    return {"error": "Failed to create user."}

def test_create_admin_user_success(requests_mock, monkeypatch, capsys, mock_response_success):
    """Test creating an admin user successfully."""
    requests_mock.post(REGISTRATION_ENDPOINT, json=mock_response_success, status_code=201)

    # Mock user input for username and password
    monkeypatch.setattr('builtins.input', lambda _: "admin_user")
    create_admin_user()

    captured = capsys.readouterr()
    assert "registered successfully" in captured.out


def test_create_admin_user_failure(requests_mock, monkeypatch, capsys, mock_response_failure):
    """Test failure in creating an admin user due to bad request."""
    requests_mock.post(REGISTRATION_ENDPOINT, json=mock_response_failure, status_code=400)

    # Mock user input for username and password
    monkeypatch.setattr('builtins.input', lambda _: "admin_user")
    create_admin_user()

    captured = capsys.readouterr()
    assert "Failed to create user" in captured.out
