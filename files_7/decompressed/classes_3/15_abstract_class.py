"""Not able to instantiate Model (abstract) class"""

from abc import ABC, abstractmethod


class Model(ABC):

    @property
    @abstractmethod
    def table(self):
        pass

    @abstractmethod
    def save(self):
        pass

    @classmethod
    def search_by_id(self, _id):
        print(f"Searching by id {_id} in table {self.table}")


class User(Model):
    table = "User"

    def save(self):
        print(f"Saving {self.table} in db.")


obj = User()
obj.save()
User.search_by_id(123)
