def extract_values(**kwargs):
    return list(kwargs.values())

print(extract_values(a=1, b=2, c=3))
print(extract_values(name="Marlena", age=26))



