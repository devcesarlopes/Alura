endereco = 'Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, RJ, 23440-120'
url = 'http://julio.com.br'
import re # Regular Expression -- RegEx

# 5 digitos + hífen (opcional) + 3 digitos

padrao = re.compile("[0-9]{5}[-]?[0-9]{3}")
busca = padrao.search(endereco) #Match
if(busca):
    print(busca.group())

busca = re.search("ulio",url)
if busca:
    print(True)