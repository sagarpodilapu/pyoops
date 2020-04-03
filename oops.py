class Parrot:
    # class attribute
    species = "bird"

    # constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    # instance method
    def dance(self):
        return "{} is now dancing".format(self.name)


# instantiation
blu = Parrot("Blu", 10)

# instantiation
woo = Parrot("Woo", 5)

# get class attribute
print("Blu is a {}".format(blu.__class__.species))
print("Woo is a {}".format(blu.__class__.species))
print("{} is {} years old".format(woo.name, woo.age))
print("{} is {} years old".format(blu.name, blu.age))

print(blu.sing("'Happy birthday'"))
print(blu.dance())
