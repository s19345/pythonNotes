import random

# Użyj pętli for, aby obliczyć sumę liczb od 1 do 100.

sum_of_numbers = 0

for i in range(1, 101):
    sum_of_numbers += i

print(f"Suma liczb od 1 do 100: {sum_of_numbers}")


# Wygeneruj tabliczkę mnożenia dla liczb od 1 do 10.

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:4}", end=" ")
    print()


# Napisz program, który wylosuje liczbę i poprosi użytkownika o zgadywanie, używając pętli
# while.

random_value = random.randint(1, 100)
print(random_value)

user_answer = None

while user_answer != random_value:
    user_answer = input('podaj liczbe: ')
    user_answer = int(user_answer)
    if user_answer != random_value:
        print('zgadnij jeszcze raz')
    else:
        print('sukces')


# Użyj all() lub any() aby zweryfikować czy wszystkie podane liczby w liście są parzyste.

# 1. all()

numbers_list = [4, 6, 6, 8]

are_all_even = all(n % 2 == 0 for n in numbers_list)

if are_all_even:
    print("Wszystkie liczby są parzyste")
else:
    print("Nie wszystkie liczby są parzyste")


# 2. any()

numbers_list1 = [4, 8, 6, 10]

are_all_even = any(n % 2 != 0 for n in numbers_list1)

if are_all_even:
    print("Nie wszystkie liczby są parzyste")
else:
    print("Wszystkie liczby są parzyste")


# Użyj all() lub any() aby zweryfikować czy jakiekolwiek słowo w liście zawiera „a” oraz „b”

word_list = ["ala", "basia", "karol"]

contain_ab = any("a" in word and "b" in word for word in word_list)

if contain_ab:
    print("Co najmniej jedno słowo zawiera 'a' oraz 'b'")
else:
    print("Żadne słowo nie zawiera zarówno 'a' jak i 'b'")


# Używając pętli, wypisz wszystkie liczby pierwsze z zakresu 1 do 100.

for i in range(1, 101):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    if counter == 2:
        print(i)



