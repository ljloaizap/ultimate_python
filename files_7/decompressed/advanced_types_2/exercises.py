"""Python Excercises"""


def run_ex_1(expression: str) -> str:
    """Removes blank spaces and returns remaining chars as a list"""
    new_exp = [c for c in expression if c != " "]

    output = new_exp
    print(output)
    return output


def run_ex_2(expression: str) -> dict:
    """Calculates how much a char is repeated in a string and presents it in dict format"""
    result_dict = {}
    for char in expression:
        result_dict[char] = int(result_dict.get(char, "0")) + 1

    output = result_dict
    print(output)
    return output


def run_ex_3(expression: str) -> tuple:
    """Orders dict by its values and returns lists of tuples"""
    dict_in = run_ex_2(expression)

    items_list = []
    for key, value in dict_in.items():
        res = (key, value)
        items_list.append(res)

    items_list.sort(key=lambda i: i[1], reverse=True)
    output = items_list
    print(output)
    return output


def run_ex_4(tuple_list: list) -> list:
    """Returns the tuple with higher value"""
    copy_list = tuple_list
    tuple_list.sort(key=lambda t: t[1], reverse=True)
    higher_value = tuple_list[0][1]

    new_list = []
    for elem in copy_list:
        if elem[1] >= higher_value:
            new_list.append(elem)
        else:
            break

    output = new_list
    print(output)
    return output


def run_ex_5(expression: str) -> str:
    """Evaluate string and indicates the capital letters that are repeated the most"""
    result_dict = {}
    for char in expression:
        result_dict[char] = int(result_dict.get(char, "0")) + 1

    # this is some sort of other functions, so skipping it for now
    return "meh"


# run_ex_1("I believe I can fly")
# run_ex_2("Loro")
# run_ex_3("cacababcd")
run_ex_4([("a", 3), ("b", 2), ("c", 4, ("d", 4))])
