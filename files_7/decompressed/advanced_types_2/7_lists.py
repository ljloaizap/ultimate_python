pets = ["Worlfgang", "Kana", "Pelusa", "Pulga", "Grenda",
        "Copito", "Lolo", "Michina", "Kana", "Harry"]
# print(pets)
# print(pets[0::2])
# print(pets[0::3])
# print(pets[0::4])
# print(pets[0::7])
# print(pets[0::8])
# print(pets[-3])

numbers = list(range(29))
# print(numbers)
# print(numbers[2::27])

first, *second, last = pets
# print(first, second, last)


output = pets.index("Pulga")
# output = pets.index("Pulgas")
output = pets.count("Kana")

pets.insert(1, "Melvin")
pets.append("Rocu")
pets.remove("Harry")
pets.pop()
pets.pop(1)
del pets[5]
pets.clear()

output = pets

# ------------------------------------------- #
# --------------- Sorting lists ------------- #
# ------------------------------------------- #
numbers = [23, 35, 12, 87, 5, 346, 95, 162, 46]
# numbers.sort()
# numbers.sort(reverse=True)
# output = sorted(numbers)

players = [
    ["Messi", 10],
    ["Zidanne", 5],
    ["C. Ronaldo", 7]
]
# players.sort()


# def order_elements(element):
#     return element[1]
# players.sort(key=order_elements)
# players.sort(key=lambda elem: elem[1], reverse=True)
output = players


# ------------------------------------------- #
# ------------ Comprehension lists ---------- #
# ------------------------------------------- #

# names = []
# for player in players:
#     names.append(player[0])
# output = names
# |
# |
# v
# names = [player[0] for player in players]
# output = names

# names = [player for player in players if player[1] > 5]
# names = [player[0] for player in players if player[1] > 5]
# output = names


# ------------------------------------------- #
# -------------- Map & Filtering ------------ #
# ------------------------------------------- #

# names = list(map(lambda p: p[0], players)) # ---> map
# output = names

# names = list(filter(lambda p: p[1] > 5, players))  # ---> filter
# output = names


# ------------------------------------------- #
# ------------------- Tuples ---------------- #
# ------------------------------------------- #
numbers = (1, 2, 3) + (4, 5, 6)
output = numbers

# point = tuple([1, 2])
# output = point

# output = numbers[:5]
# first, second, *others = numbers
# print(first, second, others)


# ------------------------------------------- #
# ------------------- Sets ------------------ #
# ------------------------------------------- #
first = {1, 1, 2, 8, 2, 3, 4, 7}
first.add(1)
first.remove(8)
output = first

second_list = [3, 4, 5]
second = set(second_list)

# Operators
print('First: ', first)
print('Second: ', second)
output = first | second  # --> |: Union
output = first & second  # --> &: Intersection
output = first - second  # --> -: Difference
output = first ^ second  # Symetric difference

if 7 in first:
    print("> Wipiti! 7 is in 'first' set.")

# ------------------------------------------- #
# ----------------- Printing ---------------- #
# ------------------------------------------- #
print(output)
