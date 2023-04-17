from .base import Base


class Products(Base):
    resource_path = "product"

    def calculate_emissions(self, **params):
        return self.client.get(f"{self.resource_path}", params=params)
