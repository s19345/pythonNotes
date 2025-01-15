counter = 0

def inc():
    global counter
    counter += 1
    return counter

print(inc())
print(inc())
print(inc())

