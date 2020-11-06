from ClassCorrida import CarroCorrida #Importando a classe de Corrida

confirmacao = False #Caso a validação de dados seja realizada com sucesso, a confirmação encerra o formulario
nomeEquipe = None #Dá o nome para a equipe do usuário
validaEquipe = None #Valida o nome da equipe do usuário
validaDados = None #Valida se os dados informados do veículo e usuário estão corretos
decisao = None #Verifica a opção da simulação escolhida pelo usuário

currentSpeed = 0.0 #velocidade atual do veiculo, não informada pelo usuário, começa em 0

print("")
user = input("Favor informar o seu nome: ") #Pegando o nome do piloto do veículo e passando para o Atributo "Piloto" da classe Corrida

print("\n" * 20) #Forma de limpar o console quebrando linhas
print("Seja bem vindo " ,user,"!")
print("Que bom te conhecer, Para iniciarmos o simulador vou te fazer algumas perguntas sobre o seu veículo. Favor responder corretamente.")
print("\n")
inicio = input("Press 'ENTER' para iniciar.")

while confirmacao == False:
    print("\n" * 30) #Forma de limpar o console quebrando linhas
    #Pegando as informações inciais do dono do veículo e sobre o seu carro
    CarroCorrida.modelo = input("Informe o modelo do carro: ")
    CarroCorrida.placa = input("Informe a placa do carro: ")
    numCar = int(input("Informe o número do carro: "))

    #Recebendo uma frase em uma variável para colocar 3 informações da classe na mesma
    inputString = "Qual é a velocidade máxima do seu {0} de placa {1} e número {2} [Km/h] : ".format(CarroCorrida.modelo, CarroCorrida.placa, numCar)
    maxSpeed = float(input(inputString)) #Passa o resultado da string com 3 valores formatados para a velocidade Máxima do veículo

    CarroCorrida.equipe = input("Informe qual é a sua equipe [A] - Alfa | [B] Beta | [O] Ômega : ")
    team = CarroCorrida.equipe #Passa o resultado da equipe para o atributo equipe da Classe

    if(team == "A" or team == "a"):
        nomeEquipe = "Alfa" #Se na equipe for informado "A" (maíusculo ou minúsculo) a equipe será a equipe Alfa
    elif(team == "B" or team == "b"):
        nomeEquipe = "Beta" #Se na equipe for informado "B" (maíusculo ou minúsculo) a equipe será a equipe Beta
    elif(team == "O" or team == "o"):
        nomeEquipe = "Ômega" #Se na equipe for informado "O" (maíusculo ou minúsculo)  a equipe será a equipe Ômega
    else:
        validaEquipe = False #Se não for informado um dos valores acima a validacao ficará inválida.
        nomeEquipe = ""

    while validaEquipe == False: #O software irá ficar perguntando até o usuário informar uma equipe válida
        print("\n" * 30) #Forma de limpar o console quebrando linhas
        print(" * Equipe inválida!")
        print(" Favor informar um dos seguintes valores [A] | [B] | [O]")
        print("")
        CarroCorrida.equipe = input("Informe qual é a sua equipe [A] - Alfa | [B] Beta | [O] Ômega : ")
        team = CarroCorrida.equipe #Passa o resultado da equipe para o atributo equipe da Classe

        if(team == "A" or team == "a"):
            nomeEquipe = "Alfa"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
        elif(team == "B" or team == "b"):
            nomeEquipe = "Beta"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
        elif(team == "O" or team == "o"):
            nomeEquipe = "Ômega"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
   
    print("\n" * 30) #Forma de limpar o console quebrando linhas

    print(" * Confirmação dos dados informados ") #Aqui será confirmado os dados informados pelo usuário
    print("")
    print("Modelo do veículo: " , CarroCorrida.modelo)
    print("Placa do veículo: " , CarroCorrida.placa)
    print("Número do veículo: " , numCar)
    print("Velocidade máxima do veículo [Km/h]: " , maxSpeed)
    print("A sua equipe é: " , nomeEquipe)
    print("")
    validaDados = input("Os dados informados acima estão corretos? [ (S) - Sim | (N) - Não ] : ") #Verificação que o usário se está certo ou não

    if(validaDados == "Sim" or validaDados == "sim" or validaDados == "S" or validaDados == "s"): #Este formulário irá repetir até o usuário informar que os dados estão corretos
        veiculo = CarroCorrida(numCar,user,team,maxSpeed,currentSpeed)
        
        confirmacao = True #O formulário será finalizado

        #Iniciando a simulação no veículo

        while decisao != 6:
            pass
            print("\n" * 20) #Forma de limpar o console quebrando linhas

            print("* Caro(a) ", user, " o que deseja fazer? ")
            print("")
            print("[1] - Ligar o veículo ")
            print("[2] - Acelerar o veículo ")
            print("[3] - Frear o veículo ")
            print("[4] - Parar o veículo ")
            print("[5] - Desligar o veículo ")
            print("[6] - Sair do veículo ")
            print("")
            decisao = int(input("Sua escolha: ")) #Decisão do usuário no simulador

            if(decisao == 1):
                CarroCorrida.chave = True #Se o usuário escolher ligar o Veículo, a chave recebe true pois ela foi girada
                CarroCorrida.ligado = True #Se o usuário girar a chave, o veículo fica em estado ligado
                print("\n" * 30) #Forma de limpar o console quebrando linhas
                print("* Você rodou a chave e ligou o veículo")
                print("")
                input("Press 'ENTER' para continuar.")
            if(decisao == 2):
                if(CarroCorrida.ligado == True): #Verifica se o carro está ligado antes de tudo

                    acelerou = veiculo.acelerar(currentSpeed,maxSpeed) #Se estiver ligado, ele usa o método de acelerar de acordo com a
                    # velocidade atual e a velocidade máxima do veículo

                    print("\n" * 30) #Forma de limpar o console quebrando linhas
                    print("* Você acelerou o veículo")
                    print("")
                    print("A velocidade atual é de: ", acelerou)
                    print("A velocidade máxima é de: ", maxSpeed)
                    input("Press 'ENTER' para continuar.")

                   
                else:
                    print("\n" * 30) #Forma de limpar o console quebrando linhas
                    print("* Você precisar ligar o veículo antes de acelerar") #O usuário tentou acelerar antes de ligar o veículo
                    print("")
                    input("Press 'ENTER' para continuar.")
                
    else:
        confirmacao = False #O formulário irá repetir




