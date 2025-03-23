# Create a dictionary containing text-type keys and values of different types
my_dict = {
    "name" : "Marlena",
    "age" : 26,
    "height" : 1.64,
    "is_student" : True
}

print(my_dict)

# Display all keys
print("Wszystkie klucze: ", my_dict.keys())

# Remove one record from the dictionary
del my_dict["height"]
print(my_dict)

# Add a new record after creating the dictionary
my_dict["city"] = "Warsaw"
print(my_dict)