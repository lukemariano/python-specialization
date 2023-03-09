"""

Tipos Imutáveis [Categoria Inicial]: str, int, float, bool

"""

# Duas variáveis apontando pra um mesmo endereço de valor na memória.
string = 'Lucas'
outra_variavel = string

print(f"id 1: {id(string)}\nId 2: {id(outra_variavel)}", end="\n#####################\n")

# Não é possível alterar o valor que possui tipos imutáveis
# string[3] = 'i'  Gera uma Exception --> TypeError: 'str' object does not support item assignment
# Uma forma de simular a 'alteração' de um valor que possui um tipo imutável é a seguinte:
# Adendo --> Slice [O final não é incluso]
simula_alterar_string = f'{string[:3]}i{string[4:]}'
print(simula_alterar_string)


# Tudo em python é objeto --> Inclusive os tipos built-in
# Os métodos de valores construidos por tipos imutáveis retornam uma cópia do valor Original.
# Eles não alteram os valores originais.
print(id(string.capitalize()))
print(string.zfill(10))


