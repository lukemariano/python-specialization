"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


numero = input('Digite um número inteiro: ')

if numero.isdigit():
    if int(numero) % 2 == 0:
        print(f'O número digitado [{numero}] é PAR.')
    else: 
        print(f'O número digitado [{numero}] é ÍMPAR.')
else:
    print('O input precisa ser um número inteiro!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Escolha uma faixa de horário entre --> 0-11, 12-17 ou 18-23: ')

if hora.isdigit():
    hora_int = int(hora) 
    if 0 <= hora_int <= 11:
        print('Bom dia!')
    elif 12 <= hora_int <= 17:
        print('Boa tarde!')
    elif 18 <= hora_int <= 23:
        print('Boa noite!')
    else:
        print('Faixa de horário inválida!')
else:
    print('A hora digita é inválida!')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite o seu nome: ')

if nome is not None and nome.isalpha():
    qtd_letras_nome = len(nome)
    if qtd_letras_nome <= 4:
        print(f'{nome} seu nome é curto.')
    elif 5 <= qtd_letras_nome <= 6:
        print(f'{nome} seu nome é normal.')
    else:
        print(f'{nome} seu nome é muito grande.')
else:
    print('Nome inválido, tente novamente!')


