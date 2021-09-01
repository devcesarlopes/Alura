# 1.3 COURSE - Python 3: Introduction to Object Orientation

## Classes e Objects

In Object Orientation, variables are called: references.
As an automatic function, it will receive a special name. We will add two _ characters before and after the name of the constructor function to create ```__init__```. Python builds the object, creates a place in memory, and then calls the ```__init__``` function. As a demonstration, the code follows:
```
>>> class Account:
        def __init__(self):
            print("Building object...")
>>> account = Account()
Building object...
```
### self
```self``` is the reference that knows how to find the object constructed in memory. Calling ```self```, you are calling the object itself.

### attributes
Now that we have the address with ```self```, we will use ```self``` to access the object and define its attributes and characteristics.
```
class Account:
    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.number = 123
        self.holder = "Nico"
        self.balance = 55.0
        self.limit = 1000.0
```

### methods
To use methods in classes, probably it's going to be required to access the object attributes. In this case, we are going to give self as parameter to the function.
```
class Account:
    def __init__(self, number, holder, balance, limit):
        print("Building object...{}".format(self))
        self.number = 123
        self.holder = "Nico"
        self.balance = 55.0
        self.limit = 1000.0
    
    def statement(self):
        print("balance {} from holder {}".format(self.balance, self.holder))
```
### Private attributes
In private attribute.
We cannot access the object's attribute directly. We will have to use the methods responsible for encapsulating object access.

So, to make the Account class attributes privates, we must restrict access to attributes, making it private, adding two underscore characters (__).
```
class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    def get_number(self):
        return(self.__number)

>>> conta = Account(123,"nico",55.2,1000.0)
>>> print(conta.get_number())
123
```

## Property
To make easier the access to attributes, python allows us to use the parameter property. 
With this parameter, we can access "directly" the attributes without calling functions.
```
class Account:

    def __init__(self, number, holder, balance, limit):
        print("Building object ... {}".format(self))
        self.__number = number
        self.__holder = holder
        self.__balance = balance
        self.__limit = limit

    @property
    def number(self):
        return(self.__number)

    @number.setter
    def number(self,number):
        self.__number = number

>>> conta = Account(123,"nico",55.2,1000.0)
>>> print(conta.number)
123
>>> conta.number = 321
>>> print(conta.number)
321
```

## Static methods
static methods that are of the class, and even without the object, we can execute the method. In some situations this can be helpful.
```
class Circle:

    def __init__(self, radius):
        print("Building object ... {}".format(self))
        self.__radius = radius
        
    @staticmethod
    def pi():
        return 3.14159265

>>> print(Circle.pi())
3.14159265
```