my_dict = {"name": "sagar", "age": 30, "IQ": 10, 1: 2}  # strings in quotes keys too
print(my_dict["name"])
print(my_dict[1])
print(my_dict.get("age"))
my_dict["age"] = 33
print(my_dict)
my_dict["skills"] = "Wow"
print(my_dict)

squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}
print(squares)
el = squares.popitem()
print(el)
print(squares)
el = squares.pop(4)
print(el)
print(squares)
del squares[3]
print(squares)
squares.clear()
print(squares)
# del squares
print(squares)

my_new_dict = my_dict.copy()
print(my_new_dict)
print(my_dict)
print(my_new_dict.items())
print(my_new_dict.keys())
print(my_new_dict.values())
for i in my_dict:
    print(i)
    print(my_dict[i])
