my_list = list([1, 2, 3])

my_list.append(4)
my_list.insert(0, 0)

print(my_list)


class CustomList(list):
    def preprend(self, item):
        self.insert(0, item)


my_list2 = CustomList([1, 2, 3])
my_list2.append(4)
my_list2.preprend(0)
print(my_list2)
