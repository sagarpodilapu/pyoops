my_tuple = ()
print(my_tuple)
my_tuple = (4, 6, 8)
print(my_tuple)
a, b, c = my_tuple
print(a, b, c)
my_tuple = ("a", "e", "i", "o", "u", "b", "d", "f")
print(my_tuple[0])
print(my_tuple[6])
my_tuple = ("sagar", [5, 6, 9], ("a", 1, 3.14), 1, 2)
print(my_tuple[0][3])
print(my_tuple[1][2])
print(my_tuple[2][1])
# my_tuple[3] = 4  # not possible
my_tuple[1][1] = 4  # this is possible
print(my_tuple)
for i in my_tuple:
    print(i)
