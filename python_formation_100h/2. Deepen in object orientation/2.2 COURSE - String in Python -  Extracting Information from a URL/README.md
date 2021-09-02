# 2.2 COURSE - String in Python -  Extracting Information from a URL

## subsring (Fatiamento)
to take a part of a string, we can do:
```
>>> position = 2
>>> text = 'abcde'
>>> text[0:position+1]
abc
>>> text[position+1:]
de
```

## Regular Expressions (Expressões Regulares) (RegEx)
to use the RegEx in python we must import the ```library re``` that is built-in
```
endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'

import re # Regular Expression -- RegEx

# 5 digitos + hífen (opcional) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-][0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) #Match
if(busca):
    print(busca.group())
```

In this case, if we type the CEP like: ```23440120``` the code won't work, because our expression is not considering the ```[-]``` as optional.
To do that, we should use: ```[-]?```
replacing in code:
```
endereco1 = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'
endereco2 = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440120'

import re # Regular Expression -- RegEx

# 5 digitos + hífen (opcional) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca1 = padrao.search(endereco1) #Match
busca2 = padrao.search(endereco2) #Match
print(busca1.group())
print(busca2.group())    
```

### Quantifiers
In order to simplify our regular expression code, we can use the quantifiers to reduce the size of the pattern. it's declared in ```{}```.
```
padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
==
padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
```

### Intervals
In order to simplify our regular expression code, we can use the intervals to reduce the size of the pattern. it's declared using ```-```, ex: ```[a-b]```.
it also can used for letters, like: 
```
padrao = re.compile("[0123456789]{5}[-]?[0123456789]{3}")
==
padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
```

### Comparing Strings
when using [] we only look for a character, but if we want to compare a string we must use: ```(string)```.

## is and ==
the difference between == and is comparators and we saw when we should use each one of them, concluding that the ```is``` operator should be used always and only when we want to compare an object's identity, that is, its memory address.

The ```==```, in turn, should be used when we want to compare values ​​(or, indeed, anything else!) of objects.
