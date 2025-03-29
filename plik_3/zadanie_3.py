# Napisz funkcję average, która przyjmuje listę liczb i zwraca ich średnią
# arytmetyczną.

def average(numbers):
    if not numbers:
        return None
    else:
        return sum(numbers) / len(numbers)

list_1 = [4, 5, 6, 7, 8]
print(average(list_1))