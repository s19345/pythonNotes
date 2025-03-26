# 1
my_list = []

for i in range(10, 101, 5):
    my_list.append(i)

# 2
for index, element in enumerate(my_list):
    print(f"Index to {index}, a element to {element}")

# for i in enumerate(my_list):
#     print(i)

# 3

my_list1 = [i for i in range(18)]

zipped = zip(my_list, my_list1)
for i in zipped:
    print(i)

