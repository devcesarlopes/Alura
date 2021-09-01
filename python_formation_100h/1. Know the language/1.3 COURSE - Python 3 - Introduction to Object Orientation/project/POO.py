class Circle:

    def __init__(self, radius):
        print("Building object ... {}".format(self))
        self.__radius = radius

    @staticmethod
    def pi():
        return 3.14159265

print(Circle.pi())