class A:
    def __init__(self, value):
        self.__value = value
    def __str__(self):
        return self.__value
    def __eq__(self, other):
        return self.__value == other
    def retunclass(self):
        return self.__class__.__name__

var = A('hello')             #var = 'hello'
print(var.retunclass())      #>>> 'A'

if var == 'hello':
    print(True)              #>>> True
