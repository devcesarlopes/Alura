# 1.2 COURSE - Python 3 part 2 - Advancing the language

## String Treatment

### String.find("str")
there's a function where we can look for something inside the ```String```. This function is find, when passing the ```str``` to it, it returns the position in the word where the ```str``` is, starting from position 0 (which represents the first letter).
```
>>> palavra = "banana"
>>> print(palavra.find("na"))
2
```
But we can notice a problem with the function, because when searching for the ```str 'na'```, the number 2 was returned, but the ```str 'na'``` also exists in position 4 of the word, but the function doesn't do that, it only returns a single position, the first that she finds.

### upper and lower case (Caixa alta e Caixa Baixa)
#### String.lower()
returns string with all lowercase letters
```
>>> palavra = "BANANA"
>>> palavra.lower()
'banana'
```
#### String.upper()
returns string with all uppercase letters
```
>>> palavra = "banana"
>>> palavra.upper()
'BANANA'
```
### String.capitalize()
retorna a string com a primeira letra em maiúsculo e o restante em minúsculo.
```
>>> palavra = "banana"
>>> palavra.capitalize()
'Banana'
```

### Remove white spaces - String.strip()
To remove the white spaces at the beggining or end of a string, we can use the function strip
```
>>> palavra = "  banana   "
>>> palavra.strip()
'banana'
```

## List
lists are a flexible kind of sequence, we can delete or add elements, and it allows repeated elements.
### Adding values List.append()
```
>>> valores = [0,1,2,3,4]
>>> valores.append(5)
>>> valores
[0,1,2,3,4,5]
```
### Accessing values
```
>>> valores = [0,1,2,3,4]
>>> valores[2]
2
```
### Min and Max
```
>>> valores = [0,1,2,3,4]
>>> min(valores)
0
>>> max(valores)
4
```
### Lenght
```
>>> valores = [0,1,2,3,4]
>>> len(valores)
5
```
### enumerate()
to get the element as well as the position of the element.
```
lista = [32, 49, 85, 79, 100]
for index, age in enumerate(lista):
        print(index, age)
0 32
1 49
2 85
3 79
4 100
```
### List Comprehension
easier way to insert elements in a list.
This works!
```
>>> frutas = ["maçã", "banana", "laranja", "melancia"]
>>> lista = []
>>> for fruta in frutas:
        lista.append(fruta.upper())
>>> lista
['MAÇÃ', 'BANANA', 'LARANJA', 'MELANCIA']
```
but this is better:
```
>>> frutas = ["maçã", "banana", "laranja", "melancia"]
>>> lista = [fruta.upper() for fruta in frutas if fruta (condition)]
>>> lista
['MAÇÃ', 'BANANA', 'LARANJA', 'MELANCIA']
```

## Tuples
if a list should be fixed, unchangeable. For that there is the tuple, which is an immutable list, it allow repeated elements.
to declare, it is the same as list, but uses ```()``` instead of ```[]```.
```
>>> days = ("sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday")
>>> type(days)
<class 'tuple'>
>>> days.append(1)
Traceback (most recent call last):  File "<stdin>", line 1, in <module> AttributeError: 'tuple' object has no attribute 'append'
```

### Converting Lists to Tuples - Tuples to List
To convert Lists to Tuples we use the command tuple(list), to do the vice-versa tuples to list, we use the command list(tuple)
```
>>> list = [0,1,2,3]
>>> list = tuple(list)
>>> type(list)
<class 'tuple'>
```

## set
sets are a flexible kind of collection, we can delete or add elements, but it doesn't allows repeated elements.
to declare, it is the same as list, but uses ```()``` instead of ```{}```.
Set doesn't use ```append()``` like the Lists, it uses ```add()``` instead.
It's important to notice Set doesn't have index. try to acces an indexed element like ```set[0]``` will result in error
```
>>> days = {"sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"}
>>> type(days)
<class 'set'>
>>> days.add("sunday")
>>> days
{"sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"}
```

## Dictionary
Dictionaries are used to store data values in key:value pairs, like Hashmaps.
```
>>> thisdict = {
        "brand": "Ford",
        "model": "Mustang",
        "year": 1964
    }
>>> print(thisdict)
{'brand': 'Ford', 'model': 'Mustang', 'year': 1964}
```

## File Manipulation
Just like C python can manipulate files.
To open a file, Python has a built-in open function. It takes two parameters: the first is the name of the file to be opened, and the second parameter is the way we want to work with this file, whether we want to read or write. The mode is passed through a string: "w" for writing, "r" for reading and "a" for append when oppening again.
### open
```
>>> arquivo = open("palavras.txt", "w")
```
### write
```
>>> arquivo.write("banana")
6
>>> arquivo.write("melancia")
8
```
### close
Quando estamos trabalhando com arquivos, devemos nos preocupar em fechá-lo. Assim como abrimos um arquivo, devemos fechá-los, chamando a função close:
```
>>> arquivo.close()
```
### read
Since we open the file in read mode, the write function doesn't work. To read the entire file, we use the read function:
```
>>> arquivo.read()
'banana\nmelancia\nmorango\nmanga\n'
```
But if we run the function again:
```
>>> arquivo.read()
''
```
We are returned an empty string. Why?

The file is like a stream of lines, starting at the beginning of the file, as if it were the pointer. It goes down and reading the file, after reading everything, it is positioned at the end of the file, so when we call the read() function again, there is no more content, as it has all been read.

In other words, to read the file again, we must close it and open it again.

### Reading line by line from file
But we don't want to read the entire contents of the file, we want to read it line by line. As we've already seen, a file is a stream of lines, a sequence of lines, so since it's a sequence, we can do a for on it:
```
>>> file = open("words.txt", "r")
>>> for line in file:
... print(line)
...
banana

watermelon

Strawberry

mango
```
