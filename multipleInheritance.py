class Base1:
    pass


class Base2:
    pass


# multiple inheritence
class MultiDerived(Base1, Base2):
    pass


# single inheritance
class Derived1(Base1):
    pass


# multiple level inheritance
class Derived2(Derived1):
    pass


print(MultiDerived.__mro__)  # returns tuple
print(Derived2.mro())  # returns array
