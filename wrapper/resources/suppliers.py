from .base import Base


class Suppliers(Base):
    resource_path = "supplier"

    def calculate_emissions(self, **params):
        return self.client.get(f"{self.resource_path}", params=params)
