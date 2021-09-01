class Account:
    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.__number = number
        self.holder = holder
        self.balance = balance
        self.limit = limit

    @property
    def number(self):
        return (self.__number)

    @number.setter
    def number(self,number):
        self.__number = number

conta = Account(123,"nico",55.2,1000.0)
conta.number = 321
print(conta.number)
A = 10
B = -9
X = A + B
print ("X = {}".format(X))