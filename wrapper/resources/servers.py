from .base import Base


class Servers(Base):
    resource_path = "servers"

    def find(self, **params):
        return self.client.get(self.resource_path, params=params)

    def retrieve(self, id):
        return self.client.get(f"{self.resource_path}/{id}")

    def calculate_emissions(self, id, **params):
        return self.client.get(f"{self.resource_path}/{id}/emissions", params=params)
