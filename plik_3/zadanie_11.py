def find_max(num):
    if len(num) == 1:
        return num[0]
    else:
        max_rest = find_max(num[1:])
        return num[0] if num[0] > max_rest else max_rest

print(find_max([3, 7, -2, 8, 5]))