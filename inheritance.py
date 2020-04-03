class Bird:
    # constructor
    def __init__(self):
        print("Bird is ready")

    # instance method
    def whoIsThis(self):
        print("Bird")

    # instance method
    def swim(self):
        print("swim faster")


# Penguin inheriting Bird
class Penguin(Bird):

    # constructor
    def __init__(self):
        super().__init__()
        print("Penguin is ready")

    # instance method
    def whoIsThis(self):
        print("Penguin")

    # instance method
    def run(self):
        print("run faster")


peggy = Penguin()
peggy.whoIsThis()
peggy.swim()
peggy.run()
