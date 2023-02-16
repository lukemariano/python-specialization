"""

Fatiamento de strings

# Acesso por index

 012345678 --> index
 Olá mundo --> str de referência
-987654321 --> index negativo

Fatiamento [i:f:p] [::]  --> dois pontos indicam o fateamento
Obs.: a função len retorna a quantidade de caracteres da string ou 
qtd de objetos de itens de um determinado objeto;

"""

variavel = 'Ola mundo'
print(variavel[-(len(variavel)):]) # index negativo é == len()
print(len(variavel))
print(variavel[0:len(variavel):2])
print(variavel[::-1])
print(variavel[-1:-10:-1])
