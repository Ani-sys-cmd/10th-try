import pytest
import requests

# 1. Define a fixture for the base URL.
@pytest.fixture
def base_url():
    """Provides the base URL for the API."""
    return "http://localhost:5000"

# 2. Write test functions for each endpoint.

def test_forgot_password(base_url):
    """
    Tests the POST /forgotPassword endpoint.
    This test sends an empty payload, which is expected to fail
    as an email is likely required. A 400 Bad Request or similar
    client error is the expected outcome.
    """
    url = f"{base_url}/forgotPassword"
    payload = {}
    response = requests.post(url, json=payload)
    
    # CRITICAL: Assert status code and print response text on failure.
    expected_status_code = 400  # Assuming 400 for missing required fields.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_reset_password(base_url):
    """
    Tests the POST /resetPassword endpoint.
    This test sends an empty payload, which is expected to fail
    as a reset token and new password are likely required. A 400 Bad Request
    is the expected outcome.
    """
    url = f"{base_url}/resetPassword"
    payload = {}
    response = requests.post(url, json=payload)
    
    expected_status_code = 400  # Assuming 400 for missing required fields.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_add_task(base_url):
    """
    Tests the POST /addTask endpoint.
    This endpoint likely requires authentication and a valid payload.
    Sending an empty payload without auth should result in an error.
    A 401 Unauthorized or 400 Bad Request is expected.
    """
    url = f"{base_url}/addTask"
    payload = {}
    response = requests.post(url, json=payload)
    
    expected_status_code = 401  # Assuming 401 as it's likely a protected route.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_get_task(base_url):
    """
    Tests the GET /getTask endpoint.
    This endpoint likely requires authentication to fetch user-specific tasks.
    An unauthenticated request is expected to fail.
    A 401 Unauthorized is the expected outcome.
    """
    url = f"{base_url}/getTask"
    response = requests.get(url)
    
    expected_status_code = 401  # Assuming 401 as it's likely a protected route.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_remove_task(base_url):
    """
    Tests the GET /removeTask endpoint.
    This endpoint likely requires authentication and a task identifier.
    An unauthenticated request is expected to fail.
    A 401 Unauthorized is the expected outcome.
    """
    url = f"{base_url}/removeTask"
    response = requests.get(url) # As specified in the prompt
    
    expected_status_code = 401  # Assuming 401 as it's likely a protected route.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_login(base_url):
    """
    Tests the POST /login endpoint.
    Sending an empty payload should fail as credentials (e.g., email, password)
    are required for login.
    A 400 Bad Request or 401 Unauthorized is the expected outcome.
    """
    url = f"{base_url}/login"
    payload = {}
    response = requests.post(url, json=payload)
    
    expected_status_code = 400  # Assuming 400 for missing credentials.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_register(base_url):
    """
    Tests the POST /register endpoint.
    Sending an empty payload should fail as user details (e.g., username, email,
    password) are required for registration.
    A 400 Bad Request is the expected outcome.
    """
    url = f"{base_url}/register"
    payload = {}
    response = requests.post(url, json=payload)
    
    expected_status_code = 400  # Assuming 400 for missing user details.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"

def test_get_user(base_url):
    """
    Tests the GET /getuser endpoint.
    This endpoint likely requires authentication to fetch user data.
    An unauthenticated request is expected to fail.
    A 401 Unauthorized is the expected outcome.
    """
    url = f"{base_url}/getuser"
    response = requests.get(url)
    
    expected_status_code = 401  # Assuming 401 as it's likely a protected route.
    assert response.status_code == expected_status_code, \
        f"Expected {expected_status_code} but got {response.status_code}. Response: {response.text}"