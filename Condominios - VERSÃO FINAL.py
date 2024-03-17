

inicializador = True
nomes_linhas = ["Bloco A", "Bloco B", "Bloco C", "Bloco D", "Bloco E",
                "Bloco F", "Bloco G", "Bloco H", "Bloco I", "Bloco J"]
valoreslista = []
matriz_principal = []
tabela_criada = False
def criar_matriz(linhas, colunas, valor):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(valor)
        matriz.append(linha)

    return matriz

def printar_matriz(matriz, nomes_linhas, nomes_andares):
    # Imprimir os rótulos dos andares
    print("BLOCOS:", end="\t      ")
    for nome_andar in nomes_andares:
        print(f"{nome_andar}", end="\t      ")
    print()

    print("=" * (10 + 15 * len(nomes_andares)))  # Linha de traços

    # Imprimir os elementos da matriz com os nomes das linhas
    for nome, linha in zip(nomes_linhas, matriz):
        print(f"{nome}| ", end="\t")
        for elemento in linha:
            print(elemento, end="\t\t")
        print()

    print("=" * (10 + 15 * len(nomes_andares)))  # Linha de traços


while inicializador:
    print("0. Criar uma base de dados")
    print("1. Inserir novo valor")
    print("2. Modificar um valor existente")
    print("3. Pesquisar por algo específico")
    print("4. Mostrar tabela de moradores")
    print("5. Sair do programa")
    print("6. Crédios do programa")

    escolherOpc = input("Digite o valor da opção que deseja: ")

    match escolherOpc:
        case "0":
        # Criando uma base de dados            
            print("Você escolheu a opc 0")
            qntBlocos = int(input("Informe a quantidade de blocos: OBS (MAX 10): "))
            qntDeAps = int(input("Informe a quantidade de andares: OBS (MAX 5): "))
            if (qntBlocos >= 1 and qntBlocos <= 10) and (qntDeAps >= 1 and qntDeAps <= 5):
                matriz_principal = criar_matriz(qntBlocos, qntDeAps, 0)
                tabela_criada = True
            else:
                print("O tamanho da matriz não está nos conformes, o o tamanho minímo é 1x1 e o máximo é 10x5")

        case "1":
        # Inserindo valores manualmente (ou não).
            # Você pode inserir valores ou deixar o programa gerar valores aleatórios
            if tabela_criada:
                inserir = input("Você deseja inserir os valores manualmente? (S/N):")
                if inserir.upper() == "S":
                    for i in range(qntDeAps * qntBlocos):
                        valores = int(input("Digite os valores: "))
                        valoreslista.append(valores)
                        if len(valoreslista) <= qntDeAps * qntBlocos:
                            matriz_principal = [valoreslista[i:i+qntDeAps] for i in range(0, len(valoreslista), qntDeAps)]           
                elif inserir.upper() == "N":
                    import random
                    for i in range(qntDeAps * qntBlocos):
                        valores = random.randint(15, 50)
                        valoreslista.append(valores)
                        if len(valoreslista) <= qntDeAps * qntBlocos:
                            matriz_principal = [valoreslista[i:i+qntDeAps] for i in range(0, len(valoreslista), qntDeAps)]
            else:
                print("Crie uma tabela com a opção 0 antes 🥱")
                input("Aperte ENTER para voltar ao menu ")


        case "2":
        # Modificando um valor existente
            # Você insere a linha e a coluna que quer modificar. 
            if tabela_criada:
                print("As linhas e as colunas começam em 1")
                linha_modificar = int(input("Digite o número da linha: "))
                coluna_modificar = int(input("Digite o número da coluna: "))           
                if linha_modificar <= qntBlocos and coluna_modificar <= qntDeAps:
                    novo_valor = int(input("Digite o novo valor: "))
                    matriz_principal[linha_modificar - 1][coluna_modificar - 1] = novo_valor
                    print("Valor modificado com sucesso!")
                else:
                    print("Posição inválida. Verifique os números da linha e coluna.")
            else:
                print("Crie uma tabela com a opção 0 antes 🥱")
                input("Aperte ENTER para voltar ao menu ")
        # Pesquisando algo específico
        case "3":
            if tabela_criada:
                print("Você escolheu a opc 3")
                qualBloco = input("Informe o bloco que deseja pesquisar: ")
                qualAndar = int(input("Informe o andar que deseja pesquisar: "))

                qualBloco = ord(qualBloco.upper()) - ord('A') + 1 #Converter Letra em número

                if 1 <= qualBloco <= 10:
                    print(f"A quantidade de moradores no andar {qualAndar} do bloco {qualBloco} é: ", matriz_principal[qualBloco - 1][qualAndar - 1])
                    input("Aperte ENTER para voltar ao menu ")
                else:
                    print("Bloco ou andar inválido. Verifique as informações e tente novamente")
            else:
                print("Crie uma tabela com a opção 0 antes 🥱")
                input("Aperte ENTER para voltar ao menu ")
        case "4":
        # Mostrando a tabela
            if tabela_criada:
                nomes_andares = []
                for i in range(qntDeAps):
                    nome_andar = f"{i + 1}º Andar"
                    nomes_andares.append(nome_andar)
                printar_matriz(matriz_principal, nomes_linhas, nomes_andares)
                input("Aperte ENTER para voltar ao menu ")
            else:
                print("Crie uma tabela com a opção 0 antes 🥱")
                input("Aperte ENTER para voltar ao menu ")
        case "5":
        # Saindo do programa
            # Você quer mesmo sair do programa? Ele está tãããão bom 😥!!
            # Se você optar por sair do programa, o sistema irá mudar o inicializador para falso, saindo do ciclo de repetição
            sair = input("Deseja mesmo sair do programa? S/N ").upper()
            if sair == "S":
                inicializador = False
                print("Até mais tarde amigoª 😎🌹")
                input("Aperte ENTER para voltar ao menu ")
            # Se você optar por ficar, por estar dentro de um while, o sistema apenas lhe mostra as opções novamente.
            elif sair == "N":
                print("Então você escolheu ficar 😏")
                input("Aperte ENTER para voltar ao menu ")
            else:
                print("Responda só com S ou N")
                input("Aperte ENTER para voltar ao menu ")
        case "6":
            print("Autor do código:\nAndré😤")
            input("Aperte ENTER para voltar ao menu ")
        case _:
            print("Digite uma opção válida 🤞")
            input("Aperte ENTER para voltar ao menu ")



