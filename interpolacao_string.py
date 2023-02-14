# Interpolação de  de string com %

"""

Interpolação básica de strings

s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789) -> estrutura

"""

nome = 'Lucas'
preco = 1000.95897643
variavel = '%s, o preço total é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal  de %d é %04x' % (15, 15))