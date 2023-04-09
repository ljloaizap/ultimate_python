
"""Polimorphism"""

from abc import ABC, abstractmethod


class Model(ABC):

    @abstractmethod
    def save(self):
        pass


class User(Model):
    def save(self):
        print("Saving in db...")


class Session(Model):
    def save(self):
        print("Saving in file...")


def save(entities):
    for entity in entities:
        entity.save()


user = User()
session = Session()

# save(user)
save([user, session])
