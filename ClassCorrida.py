#Autor: Thales Fernandes Leão
#Nome projeto: Car Simulator

class CarroCorrida: #Criando a classe de Corrida
   
    modelo = None # modelo do veículo 
    placa = None # placa do veículo

    def __init__ (self, numeroCarro, piloto, equipe, velocidadeMaxima):
        self.numeroCarro = None #Número do veículo
        self.piloto = None #Nome do piloto do veículo
        self.equipe = None #Equipe do pioloto
        self.velocidadeMaxima = 0.0 #Velocidade máxima do veículo
        self.velocidadeAtual = 0.0 #Velocidade atual do veículo
        self.chave = False #Chave de ligar e desligar o veículo
        self.estado = False # estado do veículo, parado ou movimento


    def acelerar(self, velocidadeMaxima): #Método de acelerar
        if(self.velocidadeAtual == 0.0): 
            self.velocidadeAtual = 10 #Se a velocidade for 0 ela recebe 10 para iniciar
        elif(self.velocidadeAtual <= 40): #Se a velocidade for menor ou igual a 40KM/h
            self.velocidadeAtual += (velocidadeMaxima * 0.2) #A velocidade aumenta de 20% em 20%
        elif(self.velocidadeAtual > 40 ): #Se for maior que 40
            self.velocidadeAtual += (velocidadeMaxima * 0.08) #Aumenta de 8% em 8%
            
            if(self.velocidadeAtual > velocidadeMaxima): #Se a velocidade atual passar a máxima
               self.velocidadeAtual = velocidadeMaxima #A velocidade atual recebe o seu limite

        return self.velocidadeAtual #Retorna a velocidade atual a cada acelerada

    def frear(self,velocidadeAtual):  #Método de frear o veículo
        self.velocidadeAtual -= (self.velocidadeAtual * 0.20) #Vai freando de 20% em 20%

        if(self.velocidadeAtual <= 20): #Quando a velocidade chega é menor ou igual a 20 KM/h
            self.velocidadeAtual = 0.0 #A velocidade atual vai para 0 na próxima freada

        return self.velocidadeAtual #Retorna a velocidade atual

    def parar(self,velocidadeAtual): #Método de parar o veículo
        if(velocidadeAtual != 0.0): #Se a velocidade atual for diferente de 0
            estado = True #O carro estará andando
        else:
            estado = False #O carro estará parado

        return estado

    def ligar(self): #Método de ligar o carro
        if(self.chave != True): #Se a chave não estiver girada
            self.chave = True #Ela sera girada e o veículo ligará
        

        return self.chave #Retorna o valor da chave

    def desligar(self): #Método de deslgiar o carro
        if(self.chave != False): #Se a chave estiver girada
            self.chave = False #Ela será girada ao contrário e irá deslgiar o carro

        return self.chave #Retorna valor da chave
    