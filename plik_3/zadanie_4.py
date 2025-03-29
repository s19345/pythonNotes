# Napisz rekurencyjną funkcję factorial, która obliczy silnię z danej liczby.

def average(numbers):
    if not numbers:
        return None
    else:
        return sum(numbers) / len(numbers)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

numbers = [1, 2, 3, 4, 5]
print(average(numbers))

print(factorial(5))