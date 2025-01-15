def add_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mul_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


my_dict = {"add": add_nums, "sub": sub_nums, "mul": mul_nums, "div": div_nums}


def calculator():
    operation = input("podaj działanie: ")
    num1 = int(input("podaj pierwsza liczbe: "))
    num2 = int(input("podaj druga liczbe: "))
    if operation in my_dict:
        return my_dict[operation](num1, num2)
    else:
        raise ValueError(f"Unknown operation: {operation}")


if __name__ == "__main__":
    print(calculator())

# można poprawić np umieszczając casting inputów na int w bloku try

# można też zamiast raise dać:
#     try:
#         return my_dict[operation](num1, num2)
#     except KeyError:
#         print(f"Błąd: Nieznane działanie '{operation}'")