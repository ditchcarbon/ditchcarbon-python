from .base import Base


class Activities(Base):
    resource_path = "activities"

    def retrieve(self, id):
        return self.client.get(f"{self.resource_path}/{id}")

    def retrieve_many(self, **params):
        return self.client.get(self.resource_path, params=params)

    def retrieve_assessment(self, id, **params):
        return self.client.get(f"{self.resource_path}/{id}/assessment", params=params)

    def retrieve_categories(self, **params):
        return self.client.get(f"{self.resource_path}/top-level", params=params)
