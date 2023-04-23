from .base import Base


class Expenses(Base):
    resource_path = "calculate"

    def calculate_emissions(self, **params):
        return self.client.get(f"{self.resource_path}", params=params)
