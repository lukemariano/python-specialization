"""

# Loops
while(enquanto)
Executa uma ação enquanto uma condição for verdadeira

# Infinit Loops
Loop infinito --> Quando um código não tem fim
Um dos problemas de gerar loops infinitos é que o programa irá utilizar recursos do processador
para ver o quão mais rápido ele consegue rodar esse loop.

"""

condicao = True

while condicao:
    nome = input('Digite o seu nome: ')
    print(f'O seu nome é {nome}')

    if nome.lower() == 'sair':
        break # quebra o loop | procura o laço mais próximo dessa declaração

print('Acabou')