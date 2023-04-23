from unittest.mock import MagicMock

from ditchcarbon_python import Client
from ditchcarbon_python.resources.servers import Servers


def test_find_calls_client_get_correctly():
    client = Client(token="token")
    servers = Servers(client)

    # Mock the client.get method
    client.get = MagicMock()

    # Call the find method with some params
    params = {"param1": "value1", "param2": "value2"}
    servers.find(**params)

    # Check if the client.get method was called with the correct path and params
    expected_path = servers.resource_path
    client.get.assert_called_once_with(expected_path, params=params)
