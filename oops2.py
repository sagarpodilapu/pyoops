class myClass:
    a = 10

    def func(self):
        print("Hello")


obj = myClass()
print(myClass.func)
print(obj.func)
obj.func()


class ComplexNumbers:
    def __init__(self, r=0, i=0):
        self.real = r
        self.imag = i

    def getData(self):
        print("{0}+{1}j".format(self.real, self.imag))


c1 = ComplexNumbers(1, 2)
c1.getData()

c2 = ComplexNumbers(5)
c2.attr = 10
c2.getData()
print(c2.real, c2.imag, c2.attr)
print(c1.attr)

c3 = ComplexNumbers()
c3.getData()
