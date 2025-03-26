# 1
def divide(x, y):
   result = x / y
   return result

print(divide(6, 3))

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError as e:
        print(e)
        return 42
    finally:
        print("Ten blok wykona się zawsze")

print(divide(1, 0))

# 2

def ask_for_number():
    answer = input("Podaj liczbę: ")
    try:
        int(answer)
    except ValueError as e:
        print(e)

ask_for_number()

# 3
def open_file(filepath):
    try:
        open(filepath)
    except FileNotFoundError as e:
        print(e)

open_file("test.txt")
