# Napisz program, który prosi użytkownika o podanie liczby i sprawdza, czy jest ona dodatnia,
# ujemna czy równa zero.

user_answer = int(input("Podaj liczbę: "))

if user_answer > 0:
    print("Liczba jest dodatnia")
elif user_answer < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest równa zero")


# Napisz program, który przyjmuje wynik procentowy i zwraca ocenę w skali (np. 90+ = 5, 80-89
# = 4, itd.).

score = float(input("Podaj wynik: "))

if score >= 90:
    grade = 5
elif score >= 80:
    grade = 4
elif score >= 70:
    grade = 3
elif score >= 60:
    grade = 2
else:
    grade = 1

print(f"Ocena to {grade}")


# Poproś użytkownika o liczbę i sprawdź, czy jest parzysta czy nieparzysta.

user_number = int(input("Podaj liczbę: "))

if user_number % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")


