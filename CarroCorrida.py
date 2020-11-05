from ClassCorrida import CarroCorrida #Importando a classe de Corrida

confirmacao = False
nomeEquipe = None
validaEquipe = None
validaDados = None

print("")
CarroCorrida.piloto = input("Favor informar o seu nome: ") #Pegando o nome do piloto do veículo e passando para o Atributo "Piloto" da classe Corrida

print("\n" * 20) #Forma de limpar o console quebrando linhas
print("Seja bem vindo " ,CarroCorrida.piloto,"!")
print("Que bom te conhecer, Para iniciarmos o simulador vou te fazer algumas perguntas sobre o seu veículo. Favor responder corretamente.")
print("\n")
inicio = input("Press 'ENTER' para iniciar.")

while confirmacao == False:
    print("\n" * 30) #Forma de limpar o console quebrando linhas
    #Pegando as informações inciais do dono do veículo e sobre o seu carro
    CarroCorrida.modelo = input("Informe o modelo do carro: ")
    CarroCorrida.placa = input("Informe a placa do carro: ")
    CarroCorrida.numeroCarro = int(input("Informe o número do carro: "))

    inputString = "Qual é a velocidade máxima do seu {0} de placa {1} e número {2} [Km/h] : ".format(CarroCorrida.modelo, CarroCorrida.placa, CarroCorrida.numeroCarro)
    CarroCorrida.velocidadeMaxima = float(input(inputString))

    CarroCorrida.equipe = input("Informe qual é a sua equipe [A] - Alfa | [B] Beta | [O] Ômega : ")
    nomeEquipe = CarroCorrida.equipe

    #if(nomeEquipe == "A" or nomeEquipe == "a"):
    #    nomeEquipe = "Alfa"
    #if(nomeEquipe == "B" or nomeEquipe == "b"):
    #    nomeEquipe = "Beta"
    #if(nomeEquipe == "O" or nomeEquipe == "o"):
    #    nomeEquipe = "Alfa"
    #else:
    #    print("invalido")
    

    
   
    if(CarroCorrida.equipe == "A" or CarroCorrida.equipe == "a"):
        nomeEquipe = "Alfa" #Se na equipe for informado "A" (maíusculo ou minúsculo) a equipe será a equipe Alfa
    elif(CarroCorrida.equipe == "B" or CarroCorrida.equipe == "b"):
        nomeEquipe = "Beta" #Se na equipe for informado "B" (maíusculo ou minúsculo) a equipe será a equipe Beta
    elif(CarroCorrida.equipe == "O" or CarroCorrida.equipe == "o"):
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

        if(CarroCorrida.equipe == "A" or CarroCorrida.equipe == "a"):
            nomeEquipe = "Alfa"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
        elif(CarroCorrida.equipe == "B" or CarroCorrida.equipe == "b"):
            nomeEquipe = "Beta"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
        elif(CarroCorrida.equipe == "O" or CarroCorrida.equipe == "o"):
            nomeEquipe = "Ômega"
            validaEquipe = True #Agora o usuário informou um valor válido e a validação voltou a ser True
   
    print("\n" * 30) #Forma de limpar o console quebrando linhas

    print(" * Confirmação dos dados informados ") #Aqui será confirmado os dados informados pelo usuário
    print("")
    print("Modelo do veículo: " , CarroCorrida.modelo)
    print("Placa do veículo: " , CarroCorrida.placa)
    print("Número do veículo: " , CarroCorrida.numeroCarro)
    print("Velocidade máxima do veículo [Km/h]: " , CarroCorrida.velocidadeMaxima)
    print("A sua equipe é: " , nomeEquipe)
    print("")
    validaDados = input("Os dados informados acima estão corretos? [ (S) - Sim | (N) - Não ] : ") #Verificação que o usário se está certo ou não

    if(validaDados == "Sim" or validaDados == "sim" or validaDados == "S" or validaDados == "s"): #Este formulário irá repetir até o usuário informar que os dados estão corretos
        confirmacao = True #O formulário será finalizado
    else:
        confirmacao = False #O formulário irá repetir




