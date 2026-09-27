pessoas = ["I", "You", "He", "She", "It", "We", "You", "They"]
pessoasDiferentes = ["He", "She", "It"]
Vogais = ["a", "e", "i", "o", "u"]
Consoantes = "bcdfghjklmnpqrstvwxyz"
Regra1 = ["o", "s", "x"]
while True:
    try:
        quant = int(input("========== Conjugador de Verbos em Inglês ==========\n\nDigite quantos verbos deseja: "))
        while quant < 0:
            quant = int(input("Digite novamente: "))
        break
    except ValueError:
        print()
for i in range(quant):
    verbo = input("Digite qual verbo você quer Conjugar no simple present:\nTo ")
    if verbo.lower() == "be":
        print("\nI am\nYou are\nHe is\nShe is\nIt is\nWe are\nYou are\nThey are\n")
    elif verbo.lower() == "have":
        print("\nI have\nYou have\nHe has\nShe has\nIt has\nWe have\nYou have\nThey have\n")
    else:
        verbo = verbo.lower()
        for i in pessoas:
            tamV = len(verbo)
            if i in pessoasDiferentes:
                if verbo[tamV-1:] in Regra1:
                    verboC= verbo+"es"
                    print(f"{i} {verboC} ")
                elif verbo[tamV-2:] == "ch" or verbo[tamV-2:] == "sh":
                    verboC = verbo+"es"
                    print(f"{i} {verboC}")
                elif verbo [tamV-1:] == "y":
                    verboF = verbo[tamV-2:]
                    if verboF[0] in Vogais:
                        verboC = verbo+"s"
                        print(f"{i} {verboC}")
                    else:
                        verboC = verbo[:-1]
                        verboC = verboC +"ies"
                        print(f"{i} {verboC}")
                else:
                    verboC = verbo+"s"
                    print(f"{i} {verboC}")
            else:
                print(f"{i} {verbo}")
        print()