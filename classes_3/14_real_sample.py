class Model():
    table = False

    def __init__(self):
        if not self.table:
            print("Error! You have to define a table.")

    def save(self):
        print(f"Saving {self.table} in db.")

    @classmethod
    def search_by_id(self, _id):
        print(f"Searching by id {_id} in table {self.table}")


class User(Model):
    table = "User"


user = User()
user.save()

# user.search_by_id(123)
# > add ClassMethod decorator

User.search_by_id(123)
