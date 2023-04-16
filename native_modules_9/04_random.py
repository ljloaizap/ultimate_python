import random
import string

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
my_list_2 = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(my_list)
print(
    random.random(),
    random.randint(1, 10),
    my_list,
    '--',
    random.choice(my_list_2),
    random.choices(my_list_2, k=3),
    "".join(random.choices("abcdefghi123", k=17))
)

chars = string.ascii_letters
digits = string.digits

pwd_array = random.choices(chars + digits, k=16)
pwd_str = "".join(pwd_array)
print(pwd_str)
