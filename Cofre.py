alfa = "abcdefghijklmnopqrstuvwxyz"
mensagem = input("Digite sua mensagem: ").lower()
for k in range(26):
    cripto = ""
    for i in mensagem:
        if i not in alfa:
            cripto += " "
        else:
            indice = alfa.index(i)
            indice = indice - k
            if indice < 0:
                indice = 26 + indice
                cripto += alfa[indice]
            else:
                cripto += alfa[indice]
    print(f" Chave : {k} - {cripto}\n")