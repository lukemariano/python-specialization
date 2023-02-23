"""

Introdução ao try/except
try -> tentar executar o código
except -> contingência para algum erro que possa ocorrer na execução do código

Método fail fast

"""

numero_str = input("Vou dobrar o número digitado: ")

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_float} é {numero_float * 2}')
except:
    print('Isso não é um número.')