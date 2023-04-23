import requests

from .constants import BASE_URL
from .auth import Auth
from .resources.servers import Servers
from .resources.suppliers import Suppliers
from .resources.expenses import Expenses
from .resources.products import Products
from .resources.categories import Categories
from .resources.activities import Activities


class Client:
    def __init__(self, token):
        if not token or not isinstance(token, str):
            raise ValueError("API token must be a non-empty string")

        self.base_url = BASE_URL

        self.session = requests.Session()
        self.session.auth = Auth(token)
        self.session.headers.update({"Content-Type": "application/json"})

        self.servers = Servers(self)
        self.suppliers = Suppliers(self)
        self.expenses = Expenses(self)
        self.products = Products(self)
        self.categories = Categories(self)
        self.activities = Activities(self)

    def request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.request(method, url, **kwargs)
        return response.json()

    def get(self, endpoint, **kwargs):
        return self.request("GET", endpoint, **kwargs)
