import pytest
from flask import Flask
from flask.testing import FlaskClient
from unittest.mock import patch, Mock
import json
from api import app

@pytest.fixture
def client() -> FlaskClient:
    app.testing = True
    return app.test_client()

@patch('api.get_process_data', autospec=True)
def test_get_processes_success(mock_get_process_data, client):
    # arrange
    mock_processes = [
        {"pid": 123, "name": "Process1", "cpu_percent": 10.0, "memory_info": {"rss": 1000000}},
        {"pid": 456, "name": "Process2", "cpu_percent": 20.0, "memory_info": {"rss": 2000000}}
    ]
    mock_get_process_data.return_value = mock_processes

    # act
    response = client.get('/api/processes')
    data = json.loads(response.data)

    # assert
    assert response.status_code == 200
    assert data['success']
    assert data['processes'] == mock_processes

@patch('api.get_process_data', autospec=True)
def test_get_processes_failure(mock_get_process_data, client):
    # arrange
    mock_get_process_data.side_effect = Exception("Test exception")

    # act
    response = client.get('/api/processes')
    data = json.loads(response.data)

    # assert
    assert response.status_code == 500
    assert not data['success']
    assert data['error'] == "Internal Server Error"
