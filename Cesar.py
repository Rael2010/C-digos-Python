alfa = "abcdefghijklmnopqrstuvwxyz"
aAcentuado = "áâãàä"
eAcentuado = "êèéë"
iAcentuado = "íîïì"
oAcentuado = "ôòóõö"
uAcentuado = "ùûúü"
Acentuados = aAcentuado + eAcentuado + iAcentuado + oAcentuado + uAcentuado
while True:
    try:
        key = int(input("Digite a chave para encriptar a mensagem: "))
        while key <= 0:
            key = int(input("Digite uma válida: "))
        break
    except ValueError:
        print()
mensagem = input("Digite a mensagem: \n")
cripto = ""
mensagemN = mensagem.lower()
for i in mensagemN:
    if i not in alfa and i not in Acentuados:
        cripto += i
    else:
        if i in aAcentuado:
            i = "a"
        elif i in eAcentuado:
            i = "e"
        elif i in iAcentuado:
            i = "i"
        elif i in oAcentuado:
            i = "o"
        elif i in uAcentuado:
            i = "u"
        pos = alfa.index(i)
        indice = pos+key
        if indice > 25:
            indice = indice - 26
            cripto += alfa[indice]
        else:
            letra = alfa[indice]
            cripto += letra
print(cripto)