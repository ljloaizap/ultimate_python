"""Functions"""


def say_hi(first_name, last_name="Wii"):
    print(f"Welcome, {first_name} {last_name}")


# say_hi("Chanchito", "Feliz")
# say_hi("Pepito")
# say_hi(last_name="Schurmann", first_name="Nicolas")


def sum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output


# print(sum(3, 4, 5))
# print(sum(12, 5, 3, 6))


def get_product(**data):
    print(type(data))


# get_product(first_name="Lili", last_name="Loaiza", id="123")


def get_length(text):
    count = 0
    for _ in text:
        count += 1
    return count


# who = "Chanchito"
# print(who)
# my_len = get_length("Palomino")


def is_palindrom(word):
    word_lower = word.lower()
    new_word = ""
    for char in word_lower:
        if char != " ":
            new_word += char

    length = len(new_word)
    build = ""
    for idx in range(0, length):
        build += new_word[length - idx - 1]
    output = "Yes" if new_word == build else "No"
    print(f"Is palindrom? '{word}' > {output}")


is_palindrom("reconocer")
is_palindrom("reconocera")
is_palindrom("Anita lava la tina")
is_palindrom("amooma")
is_palindrom("Neyen")
