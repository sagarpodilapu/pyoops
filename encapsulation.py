class Computer:
    def __init__(self):
        # private __
        self.__maxprice = 800
        # public
        self.brand = "HP"
        # protected _
        self._discount = 100

    def sell(self):
        print(
            "{} selling Price: {} and discount is {}".format(
                self.brand, self.__maxprice, self._discount
            )
        )

    def setMaxPrice(self, price):
        self.__maxprice = price


c = Computer()
c.sell()

c.brand = "Macbook"
# cant change private
c.__maxprice = 1000

c.sell()
# can change protected
c._discount = 200
c.setMaxPrice(1000)
c.sell()
