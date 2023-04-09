"""Dictionaries"""

point = {
    "x": 25,
    "y": 50
}

# ------------------------------------------- #
# ----------- Unpacking operator ------------ #
# ------------------------------------------- #
point["z"] = 45
# print(point.get("lala", "noonee"))
output = point

del point["x"]
del (point["y"])
output = point

point["x"] = 25

# for key in point:
#     print(point[key])

# for i in point.items():
#     print(i)

# for key, value in point.items():
#     print(f"Key: {key}, Value: {value}")


users = [
    {"id": 1, "name": "Aldemar"},
    {"id": 2, "name": "Inés"},
    {"id": 3, "name": "Brian"},
    {"id": 4, "name": "Lolo"}
]

# for user in users:
#     print(user["id"], user["name"])


# my_list = [1, 2, 3, 4]
# print(my_list)
# print(*my_list)

# my_list_2 = [5, 6]
# mixed = ["Hola", *my_list, True, *my_list_2, "Mundo"]
# output = mixed


# Unpacking with dictonary
obj1 = {"x": 26, "y": "hola"}
obj2 = {"y": 47}
new_obj = {**obj1, **obj2, "x": "mundo", "active": True}
output = new_obj


# ------------------------------------------- #
# ----------------- Printing ---------------- #
# ------------------------------------------- #
print(output)
