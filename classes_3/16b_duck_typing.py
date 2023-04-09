"""Duck typing"""


class User:
    def save(self):
        print("Saving in db...")


class Session:
    def save(self):
        print("Saving in file...")


def save(entities):
    for entity in entities:
        entity.save()


user = User()
session = Session()

# save(user)
save([user, session])
