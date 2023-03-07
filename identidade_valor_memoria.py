"""

Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade

"""

# ID SECTION 


# as duas variáveis apontam para o mesmo valor na memória
# o python busca os valores pelo id --> sua identidade na memória
v1 = 'a' # apelido para uma coisa que está na memória
v2 = 'a'
print(id(v1))
print(id(v2))

##########################################################################################

# Flags, is, is not e None 

condicao = True
passou_no_if = None # Flag

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# Normalmente o operador 'is' é utilizado junto com o valor 'None'
print(passou_no_if, passou_no_if is None)
print(passou_no_if, passou_no_if is not None)



