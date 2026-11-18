# aAcentuado = "áâãàä"
# eAcentuado = "êèéë"
# iAcentuado = "íîïì"
# oAcentuado = "ôòóõö"
# uAcentuado = "ùûúü"
# Acentuados = aAcentuado + eAcentuado + iAcentuado + oAcentuado + uAcentuado
# alfa = "abcdefghijklmnopqrstuvwxyz"
# key = input("Digite a chave da cifra: ")
# mensagem = input("Digite a mensagem que deseja criptografar: ")
# tamKey = len(key)
# while len(mensagem) < tamKey:
#     mensagem = input("Digite uma mensagem com tamanho maior ou igual a chave: ")
# mensagemV = mensagem.lower()
# keyN = key.lower()
# cripto = ""
# tamKey = len(keyN)
# while tamKey < len(mensagem):
#     keyN += keyN
#     tamKey = len(keyN)
# repet = 0
# for i in mensagemV:
#     if i not in alfa and i not in Acentuados:
#         cripto += i
#     else:
#         if i in aAcentuado:
#             i = "a"
#         elif i in eAcentuado:
#             i = "e"
#         elif i in iAcentuado:
#             i = "i"
#         elif i in oAcentuado:
#             i = "o"
#         elif i in uAcentuado:
#             i = "u"
#         posI = alfa.index(i)
#         novaLetra = posI + alfa.index(keyN[repet])
#         if novaLetra > 25:
#             novaLetra -= 26
#             cripto += alfa[novaLetra]
#         else:
#             cripto += alfa[novaLetra]
#     repet += 1
# print(cripto)
for i in range(2**32):
    A = 1
print("Terminei")