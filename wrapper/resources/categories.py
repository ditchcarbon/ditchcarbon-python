from .base import Base


class Categories(Base):
    resource_path = "categories"

    def search(self, **params):
        return self.client.get(f"{self.resource_path}", params=params)
