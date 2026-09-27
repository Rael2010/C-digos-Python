EscolaDados = {
    "Pré escola":{},
    "1Ef": {},
    "2Ef": {},
    "3Ef": {},
    "4Ef": {},
    "5Ef": {},
    "6Ef": {},
    "7Ef": {},
    "8Ef": {},
    "9Ef": {},
    "1EM": {},
    "2EM": {},
    "3EM": {},
    "4EM": {}
}
def cadastro():
    while True:
        try:
            quant = int(input("Quantidade de aluno(a)s que serão cadastrados: "))
            while quant < 0:
                quant = int(input("Digite um número válido: "))
            break
        except ValueError:
            print("Carácteres inválidos: ")
    serie = input("Qual série será cadatrada: ")
    while serie not in EscolaDados.keys():
        serie = input("Digite uma série válida: ")
    for i in range(quant):
        nome = input("Digite o nome do aluno(a)/a: ")
        while nome in EscolaDados[serie]:
            nome = input("aluno(a) repetido: ")
        while True:
            try:
                ano = int(input(f"Digite o ano em que {nome} nasceu: "))
                while ano < 0:
                    ano = int(input("Digite um ano válido: "))
                break
            except ValueError:
                print("")
        def Bissexto(ANO):
            Dezena = int(str(ANO)[-2:])
            ÉBissexto = False
            if Dezena != 00 and Dezena %4 == 0:
                ÉBissexto = True
            elif Dezena == 00 and ANO % 400 == 0:
                ÉBissexto = True
            return ÉBissexto
        teste = Bissexto(ano)
        meses = {
            "JANEIRO": {
                "Abreviado" : "1", "Dias" : 31
            },
            "FEVEREIRO" : {
                "Abreviado": "2", "Dias" : 28
            },
            "MARÇO" :{
                "Abreviado": "3", "Dias": 31
            }, 
            "ABRIL"  : {
                "Abreviado": "4", "Dias": 30
            },
            "MAIO" : {
                "Abreviado": "5", "Dias": 31
            },
            "JUNHO" : {
                "Abreviado": "6", "Dias": 30
            },
            "JULHO" : {
                "Abreviado":  "7", "Dias": 31
            },
            "AGOSTO" : {
                "Abreviado":  "8", "Dias": 31
            },
            "SETEMBRO" : {
                "Abreviado": "9","Dias": 30
            },
            "OUTUBRO" :{
                "Abreviado": "10", "Dias": 31
            },
            "NOVEMBRO"  : {
                "Abreviado": "11", "Dias": 30
            },
            "DEZEMBRO"  : {
                "Abreviado": "12", "Dias": 31
            }
        }
        if teste == True:
            meses["FEVEREIRO"]["Dias"] = 29
        mes = input(f"Digite o mês que {nome} nasceu: ")
        while mes.upper() not in meses:
            mes = input("Digite um mês valido: ")
        while True:
            try:
                dia = int(input(f"Digite o dia que {nome} nasceu: "))
                while dia < 1 or dia > meses[mes.upper()]["Dias"]:
                    dia = int(input("Digite um dia válido: "))
                break
            except ValueError:
                print("")
        datanasc = str(dia) + "/" + meses[mes.upper()]["Abreviado"] + "/" + str(ano)
        while True:
            try:        
                cpf = input(f"Digite o cpf de {nome}: ")
                while  len(cpf) != 11:
                    cpf = (input("Digite um cpf válido: "))
                break
            except ValueError:
                print("Carácteres inválidos.\n")
        turno = input(f"Digite o turno em que {nome} estuda: ")
        while turno.upper() not in ["TARDE", "MANHA", "MANHÃ"]:
            turno = input("Digite um turno válido: ")        
        EscolaDados[serie][nome] = {}
        EscolaDados[serie][nome]["Nome"] = nome
        EscolaDados[serie][nome]["Data de Nascimento"] = datanasc
        EscolaDados[serie][nome]["CPF"] = cpf
        EscolaDados[serie][nome]["Turno"] = turno.upper()
        print("aluno(a) cadastardo com sucesso.\n")
def Listar():
    cont = 1
    for turmas, aluno in EscolaDados.items():
        print(f"aluno(a)s do(a) {turmas}:")
        if not EscolaDados[turmas]:
            print(f"Nenhum aluno(a) cadastrado no {turmas}")
        else:
            for chaves in aluno.keys():      
                print(f"{cont}º-{chaves}.")
                cont+= 1
        print()    
        cont = 1
def Ver_aluno():
    continuar = 0
    while continuar == 0:
        serie = input("Diga a série do aluno(a): ")
        while serie not in EscolaDados:
            serie = input("Diga uma série válida: ")
        if not EscolaDados[serie]:
            print(f"Nenhum aluno(a) cadastrado no(a) {serie}.\n")
            continuar = 1
        else:
            nome = input("Diga o nome do aluno(a): ")
            while nome not in EscolaDados[serie]:
                nome = input("Digite o nome de um aluno(a) desta série: ")
            for chaves, dados in EscolaDados[serie][nome].items():
                if chaves == "Notas":
                    continuar = 1
                print(f"{chaves} : {dados}")
            print("")
            continuar = 1   
def Notas():
    def InserirNotas(A1, Tipo, ):
        while True:
            try:
                A1 = int(input(f"Digite a nota do(a) {Tipo}: "))
                while A1 < 0 or A1 > 10:
                    A1 = int(input(f"Digite uma nota valida: "))
                break  
            except ValueError:
                print("")
        return A1
    continuar = 0
    while continuar == 0:
        trimestres = ["1º Trimestre", "2º Trimestre", "3º Trimestre"]
        avali = ["Prova", "Trabalho", "Atividades"]
        matériasFundUm = ["Matemática", "Português", "História", "Geografia", "Ensino Religioso", "Ciências"]
        matériasFundDois = ["Matemática", "Português", "História", "Geografia", "Ensino Religioso", "Ciências", "E.D Física", "Artes", "Inglês"]
        matériasMédio = ["Matemática", "Português", "História", "Geografia", "Biologia", "Química", "Física","Sociologia", "Educação Física", "Inglês", "Espanhol", "Filosofia", "Artes", ]
        serie = input("Digite a serie que o aluno(a) se encontra: ")
        while serie not in EscolaDados:
            serie = input("Digite uma série Válida: ")
        if serie in ["Pré escola", "1Ef", "2Ef", "3Ef"]:   
            if not EscolaDados[serie]:
                print(f"Nenhum aluno(a) cadastrado em {serie} .\n") 
                continuar = 1
            else:
                nome = input("Digite o nome do aluno(a) que será inserido as notas: ")
                while nome not in EscolaDados[serie]:
                    nome = input("Insira o nome de um aluno(a) presente: ")
                EscolaDados[serie][nome]["Notas"] = {}   
                for i in range(3):
                    for j in range(3):
                        Nota = 0
                        Tipo = avali[j] + "do" + trimestres[i] 
                        Nota = InserirNotas(Nota, Tipo)
                        EscolaDados[serie][nome]["Notas"][trimestres[i]][avali[j]] = Nota
                print("Notas cadastradas com sucesso\n")
            continuar = 1
        elif serie in ["4Ef", "5Ef"]:
            continuar = 0
            avalif = ["Prova", "Trabalho", "Exercícios"]
            while continuar == 0:
                if not EscolaDados[serie]:
                    print(f"Nenhum aluno(a) cadastrado em {serie} .\n")
                    continuar = 1
                else:
                    nome = input("Digite o nome do aluno(a) que será inserido as notas: ")
                    while nome not in EscolaDados[serie]:
                        nome = input("Digite o nome de um aluno(a) válido: ")
                    EscolaDados[serie][nome]["Notas"] = {}
                    EscolaDados[serie][nome]["Notas"]["1º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["2º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["3º Trimestre"] = {} 
                    for i in range(3):
                        for j in range(6):
                            EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundUm[j]] = {}
                    for i in range(3):
                        for j in range(6):
                            for k in range(3):
                                Tipo = avalif[k]  + " de " + matériasFundUm[j] + " do " + trimestres[i]
                                Nota = 0
                                Nota = InserirNotas(Nota, Tipo )
                                EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundUm[j]][avalif[k]] = Nota
                            soma = 0
                            for NT in EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundUm[j]].values():
                                soma += NT*3.333333333333
                            MédiaTrimestre = soma/10
                            EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundUm[j]]["Média"] = MédiaTrimestre
                    print("Notas cadastradas com sucesso.\n")
                    continuar = 1
        elif serie in ["6Ef", "7Ef", "8Ef", "9Ef"]:
            continuar = 0
            avalif = ["Prova","Trabalho","Exercios"]
            while continuar == 0:
                if not EscolaDados[serie]:
                    print(f"Nenhum aluno(a) cadastrado em {serie} .\n")
                    continuar = 1
                else:
                    nome = input("Digite o nome do aluno(a) que será inserido as notas: ")
                    while nome not in EscolaDados[serie]:
                        nome = input("Digite o nome de um aluno(a) válido: ")
                    EscolaDados[serie][nome]["Notas"] = {}
                    EscolaDados[serie][nome]["Notas"]["1º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["2º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["3º Trimestre"] = {}
                    for i in range(3):
                        for j in range(9):
                            EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundDois[j]] = {}
                    for i in range(3):
                        for j in range(9):
                            for k in range(3):
                                Tipo = avalif[k] + " de " + matériasFundDois[j] + " do " + trimestres[i]
                                Nota = 0
                                Nota = InserirNotas(Nota, Tipo)
                                EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundDois[j]][avalif[k]] = Nota
                            print("______________________________________")
                            soma = 0
                            for nota in EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundDois[j]].values():
                                soma += nota*3.333333333333
                            MédiaTrimestre = soma/10
                            EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasFundDois[j]]["Média"] = MédiaTrimestre
                    print("Notas cadastradas com sucesso. \n")
                    continuar = 1
        else:
            if not EscolaDados[serie]:
                print(f"Nenhum aluno(a) cadastrado no {serie} .\n")
                continuar = 1
            else:
                nome = input("Digite o nome do aluno(a): ")
                while nome not in EscolaDados[serie]:
                    nome = input("Digite um nome válido")
                    EscolaDados[serie][nome]["Notas"] = {}
                    EscolaDados[serie][nome]["Notas"]["1º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["2º Trimestre"] = {}
                    EscolaDados[serie][nome]["Notas"]["3º Trimestre"] = {}
                    for i in range(3):
                        for j in range(13):
                            for k in range(3):
                                Nota = 0
                                Tipo = avalif[k] + " de " + matériasMédio[j] + " do " + trimestres[i]
                                Nota = InserirNotas(Nota, Tipo)
                                EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasMédio[j]][avalif[k]] = Nota
                            print("_____________________________________")
                            soma = 0
                            for NT in EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasMédio[j]].values():
                                soma += NT*3.3
                            MédiaTrimestre = soma/10
                            EscolaDados[serie][nome]["Notas"][trimestres[i]][matériasMédio[j]]["Média"] = MédiaTrimestre
                    print("Notas cadastradas com sucesso .\n")
                    continuar = 1              
def MostrarNotas():
    continuar = 0
    while continuar == 0:
        serie = input("Digite em qual série está o aluno(a): ")
        while serie not in EscolaDados:
            serie = input("Digite uma série válida: ")
        if serie in ["Pré escola", "1Ef", "2Ef", "3Ef"]:
            if not EscolaDados[serie]:
                print("Não há nenhum aluno(a) presente nesta série.\n")
                continuar = 1
            else:
                nome = input("Digite o nome do aluno(a): ")
                while nome not in EscolaDados[serie]:
                    nome = input("Digite um nome válido: ")
                if "Notas" not in EscolaDados[serie][nome]:
                    print(f"Nenhuma nota foi cadastrada no perfil de {nome} .\n")
                    continuar = 1
                else:
                    for Trimestre in EscolaDados[serie][nome]["Notas"].keys():
                        print(f"Notas do {Trimestre}: ")
                        for Aval, nt in EscolaDados[serie][nome]["Notas"][Trimestre].items():
                            print(f"{Aval} : {nt:.2f}\n----------------------------")
                        print("")
            continuar = 1
        elif serie in ["4Ef", "5Ef"]:
            if not EscolaDados[serie]:
                print("Não há nenhum aluno(a) presente nesta série. \n")
                continuar = 1
            else:
                nome = input("Digite o nome do aluno(a): ")
                while nome not in EscolaDados[serie]:
                    nome = input("Digite um nome válido: ")
                if "Notas" not in EscolaDados[serie][nome]:
                    print(f"Nenhuma nota foi cadastrada no perfil de {nome} .\n")
                    continuar = 1
                else:
                    for Trimestre in EscolaDados[serie][nome]["Notas"].keys():
                        print(f"Notas do {Trimestre}: ")
                        for Matéria, NT in EscolaDados[serie][nome]["Notas"][Trimestre].items():
                            print(f"{Matéria}:")
                            for NT , N in EscolaDados[serie][nome]["Notas"][Trimestre][Matéria].items():
                                if NT == "Média":
                                    print(f"{NT} : {N:.2f}\n---------------------------")
            continuar = 1
        elif serie in ["6Ef", "7Ef", "8Ef", "9Ef"]:
            if not EscolaDados[serie]:
                print("Não há nenhum aluno(a) presente nesta série. \n")
                continuar = 1
            else:
                nome = input("Digite o nome do aluno(a): ")
                while nome not in EscolaDados[serie]:
                    nome = input("Digite o nome de um aluno(a) válido: ")
                if "Notas" not in EscolaDados[serie][nome]:
                    print(f"Nenhuma nota foi cadastrada no perfil de {nome}")
                    continuar = 1
                else:
                    for Trimestre in EscolaDados[serie][nome]["Notas"].keys():
                        print(f"Notas do {Trimestre} ")
                        for Matéria, NT in EscolaDados[serie][nome]["Notas"][Trimestre].items():
                            print(f"{Matéria}:")
                            for Nt, N in EscolaDados[serie][nome]["Notas"][Trimestre][Matéria].items():
                                if Nt == "Média":
                                    print(f"{Nt} : {N:.2f}\n-----------------")
                        print("_______________________")
            continuar = 1
        else:
            nome = input("Digite o nome do aluno(a)(a): ")
            while nome not in EscolaDados[serie]:
                nome = input("Digite um nome válido: ")
            if "Notas" not in EscolaDados[serie][nome]:
                print(f"Nenhum nota foi cadastrada no perfil de {nome}")
                continuar = 1
            else:
                for Trimestre in EscolaDados[serie][nome]["Notas"].keys():
                    print(f"Notas do {Trimestre}")
                    for Matéria in EscolaDados[serie][nome]["Notas"][Trimestre].keys():
                        print(f"Notas de {Matéria}")
                        for Nt, N in EscolaDados[serie][nome]["Notas"][Trimestre][Matéria].items():
                            if Nt == "Notas":
                                print(f"{Nt} : {N}\n--------------------") 
                        print("____________________________")         
while True:
    ação = input("Escolha uma ação:\n1-Cadastrar aluno(a).\n2-Listar aluno(a)s.\n3-Ver aluno(a).\n4-Inserir notas(Em produção.)\n5-Ver Notas(Em Produção)\nDigite aqui: ")
    while ação not in ['1', '2', '3','4', '5']:
        ação = input("Digite uma ação válida: ")
    match ação:
        case "1":
            cadastro()
        case "2":
            Listar()
        case "3":
            Ver_aluno() 
        case "4":
            Notas()
        case "5":
            MostrarNotas()