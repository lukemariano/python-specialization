# utilizando continue apenas para revisar o básico do básico do básico (ironia com repetição)

contador = 0

while contador < 10:
    contador += 1

    if contador == 5:
        print('pulei o número 5')
        continue # pula para o próximo loop/laço

    print(contador)