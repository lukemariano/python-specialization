"""

Formatação básica de strings com f-strings

s - string
d - int
f - float
.<número de digítos>f
x ou X - Hexadecimal
(Caractere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o número a aparecer antes dos zeros
Sinal - + ou -
Ex: 0>-100,.1f
Conversion flags - !r (__repr__) !s (__str__) !a (__asc__)

"""

variavel = 'ABC'
print(variavel)
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.11243:0=+10,.1f}')
print(f'O hexadecimal de 1500 é: {1500:08X}')
print(f'{variavel!r}')
