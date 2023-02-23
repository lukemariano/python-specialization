"""

Peça ao usuário para digitar o seu nome
Peça ao usuário para digitar sua idade
Se o nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}

Se nada for digitado em nome ou idade:
    exiba "Desculpe, você deixou campos vazios."
   
"""

nome = input("Digite o seu nome: ")
idade = input("Digite a sua idade: ")

try:
    # valida idade
    int(idade)

    # outputs desejados
    nome_invertido = nome[::-1]
    tem_espaco = "contém" if " " in nome else "não contém"
    qtd_letras = len([letra for letra in nome if letra != " "])
    primeira_letra = nome[0]
    ultima_letra = nome[-1]
  

    if not nome or not idade:
        print("Desculpe, você deixou campos vazios.")
    else:
        print(f"Seu nome é {nome}")
        print(f"Seu nome invertido é {nome_invertido}")
        print(f"Seu nome {tem_espaco} espaços")
        print(f"Seu nome tem {qtd_letras} letras")
        print(f"A primeira letra do seu nome é: {primeira_letra}")
        print(f"A última letra do seu nome é: {ultima_letra}")
except:
    print("Idade inválida!")