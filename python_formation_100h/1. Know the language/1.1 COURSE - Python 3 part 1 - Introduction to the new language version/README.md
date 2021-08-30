# Python 3 part 1: Introduction to the new language version

We were also able to use Python without installing it on our machine, running it through a web service. There are several websites that offer this service, including [repl.it](https://replit.com/).


## Print()

print can receive:

value is the value we want to print, the ellipses indicate that the function can receive more than one value, just separate them with a comma.
sep is the separator between values, by default the separator is a blank.
end is what will happen at the end of the function, by default there is a newline, a newline (\n).
We can press the Q key to exit the function documentation and CTRL + C or CTRL + D to exit the Python help console. Back in Python's own console, we can test the print function with the values ​​we saw:
```
>>> print("Brazil", "won", 5, "world titles", sep="-")
Brazil-won-5-world titles
```
As we modified the separator, the values ​​are now separated by a hyphen. Let's test the end now, not passing anything to it:
```
>>> print("Brazil", "won", 5, "world titles", end="")
Brazil won 5 world titles>>>
```
A new line is not created, that is, what we put inside the end will be printed at the end of the function.

## type()

The variable's type depends on the value we pass to it. We can "ask" the variable what its type is by passing it to the type function:
```
>>> type(parents)
<class 'str'>
>>> type(amount)
<class 'int'>
```
The value str means that the variable is of type string, as its value is enclosed in double quotes. And int means the variable is of type integer, since we pass an integer value to the variable.

## Variables
Knowing that Python uses dynamic typing, a variable only exists when we assign a value.
There is no static variable declaration in Python, as in languages ​​like C, Java or C#. In these languages, we indicate the type and name of the variables and it already exists.
For example:
```
int age;
```
Note that we only declare the variable's type and name, without having assigned the value.
In Python, the variable only exists when we assign a value, as in the example below:
```
age = 12
```
This makes perfect sense since we don't have an explicit type declaration like in the Java or C# language.

## Variable Patterns (Snake_Case)
Python conventionally uses the Snake_Case pattern for variable names (or identifiers).

An example of variables in Snake_Case are:
```
wife_age = 20
profile_vip = 'Flávio Almeida'
receipts_in_delay = 30
```
In other languages ​​the CamelCase pattern is also used. Same example with CamelCase (which is not the Python default):
```
Wife age = 20
VIPprofile = 'Flávio Almeida'
receiptsOverdue = 30COPY CODE
```
Let's follow the Python pattern in this course, which is Snake_Case!
