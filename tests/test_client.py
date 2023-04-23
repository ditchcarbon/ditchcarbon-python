import pytest
from unittest.mock import MagicMock

from ditchcarbon_python import Client
from ditchcarbon_python.auth import Auth
from ditchcarbon_python.resources.servers import Servers


def test_invalid_token():
    with pytest.raises(ValueError, match="API token must be a non-empty string"):
        client = Client(token=None)

    with pytest.raises(ValueError, match="API token must be a non-empty string"):
        client = Client(token="")


def test_session_and_auth():
    token = "token"
    client = Client(token=token)

    assert hasattr(client, "session")
    assert hasattr(client.session, "auth")
    assert isinstance(client.session.auth, Auth)
    assert client.session.auth.token == token


def test_client_resource_instances():
    client = Client(token="token")

    assert hasattr(client, "servers")
    assert isinstance(client.servers, Servers)


def test_get_url_construction():
    token = "token"
    client = Client(token=token)

    # Mock the client.session.request method
    client.session.request = MagicMock()

    # Call the get method with a path and some params
    path = "servers"
    params = {"param1": "value1", "param2": "value2"}
    client.get(path, params=params)

    # Check if the client.session.request method was called with the correct path and params
    expected_url = f"{client.base_url}/{path}"
    client.session.request.assert_called_once_with("GET", expected_url, params=params)
