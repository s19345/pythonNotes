# stwórz listę:
# 1. zawierającą liczby od 1 do 100
list_1 = [x for x in range(1, 101)]


# zawierającą tylko liczby parzyste od 1 do 100
list_2 = [x for x in range(1, 101) if x % 2 == 0]


# zawierającą liczby od 1 do 100 które NIE znajdują się w liście c ([5,44,13,25]).
list_3 = [x for x in range(1, 101) if x not in [5,44,13,25]]



# Dwuwymiarową, zawierającą 100 list, posiadających 1,2,3,4,5… elementów: [ [1], [1,2],
# [1,2,3]…]
list_4 = [[x for x in range(1, y + 1)] for y in range(1, 101)]


# zawierającą potęgi liczb od 1 do 10
list_5 = [x ** x for x in range (1, 11) ]


# zawierającą liczby od 1 do 100 NIE podzielnych przez 6 i 4
list_6 = [x for x in range(1, 101) if x % 6 != 0 and x % 4 != 0]


# zawierającą 10 list pustych
list_7 = [[] for x in range(10)]



#  zawierającą wszystkie litery oprócz „e” oraz „c” ze zmiennej s = „Python jest językiem
# posiadającym różne cechy.”
s = "Python jest językiem posiadającym różne cechy."
list_8 = [x for x in s if x not in ['e', 'c'] and x.isalpha()]


# Zawiera tylko liczby z podanej zmiennej tekstowej: zM7U0AS1J3jj09Afj!?
variable = 'zM7U0AS1J3jj09Afj!?'

list_9 = [x for x in variable if x.isdigit()]


