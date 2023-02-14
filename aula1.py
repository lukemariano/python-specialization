# \r\n -> CRLF (Mac os) / Carriage return
# \n -> LF (Linux) / line feed
# Variáveis são utilizadas para salvar algo na memória do computador
# Módulo retorna se um número é divisivel / múltiplo de outro número
# python -i <module_name> --> carrega o módulo no power shell e pode-se utilizar qualquer variável;
# posso quebrar o código com diferentes f-strings

soma = '2 + 2'
print(154, 856, sep="-", end=" $$$$\n")
print('a' < 'b')
print(
    f'Uma linha\n' 
    f'Duas linhas'
)

# avaliação de curto circuito
print(True and False and True) # já stopa na primeira condição falsa

# avaliação de curto circuito parte 2

# retorna a primeira expressão verdadeira com seu respectivo valor
senha = input('Senha: ') or 'Sem senha'
print(senha)

# strings são iteráveis -> operadores 'in' e 'not in' iteram sobre elas
# para realizarem checagens
print(10 * '-')
print('L' in 'Lucas')
