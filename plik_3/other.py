#closure (można użyć w zadaniu 7 do licznika, wtedy zmienna cls jest tym counterem)

def closure():
    counter = 0

    def inner():
        nonlocal counter
        counter += 1
        return counter

    return inner


cls = closure()

print(cls())
print(cls())
print(cls())

# zasięg zmiennych

counter = "ala"


def increment():
    global counter
    print(counter)
    counter = 1

    def increment2():
        global counter
        print(counter)
        counter = 2
        return counter

    return counter


# typing i __doc__ (zad 14 i 15), (w pliku z zad 15 możesz zaimportować funkcję z 14)

def func1(name: str, age: int) -> str:
    """
    ta funkcja coś tam robi
    """
    a = f'hello {name}, im {age} old'
    print(a)
    return a


func1("Marlena", 18)

print(dir(func1))

print(func1.__doc__)

# tu tłumaczyłem argsy i kwargsy:
def sum_all(*ala, **yolo):
    print(ala)
    print(ala[0])
    print(yolo["a"])
    print(yolo.get("klucz", "nie ma"))
    return sum(ala)

sum_all(1, 2, 3, 4, 8, a=6, b=7,)