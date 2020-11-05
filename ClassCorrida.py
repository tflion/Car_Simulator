class CarroCorrida:
   
    modelo = None # modelo do carro 
    placa = None # placa do carro
    numeroCarro = None # numero do carro para a corrida
    piloto = None # nome do piloto
    equipe = None # equipe do piloto
    velocidadeMaxima = None # velocidade máxima do veículo
    velocidadeAtual = None
    estado = None
    ligado = None
    chave = None


    def __init__ (self, numeroCarro, piloto, equipe, velocidadeMaxima):
        self.numeroCarro = None
        self.piloto = None
        self.equipe = None
        self.velocidadeMaxima = None

    def acelerar(self,velocidadeAtual, velocidadeMaxima):
        if(self.velocidadeAtual == 0):
            self.velocidadeAtual = 10
        elif(self.velocidadeAtual <= 40):
            self.velocidadeAtual += (self.velocidadeMaxima * 2.0)
        elif(self.velocidadeAtual > 40 and self.velocidadeAtual < self.velocidadeMaxima):
            self.velocidadeAtual += (self.velocidadeMaxima * 0.8) 
            
            if(self.velocidadeAtual > self.velocidadeMaxima):
                self.velocidadeAtual = self.velocidadeMaxima

    def frear(self,velocidadeAtual):
        self.velocidadeAtual -= (self.velocidadeAtual * 0.20)

        if(self.velocidadeAtual <= 20):
            self.velocidadeAtual = 0

    def parar(self,velocidadeAtual,estado):
        if(velocidadeAtual != 0):
            estado = True
        else:
            estado = False

    def ligar(self, chave, ligado):
        if(chave == True):
            ligado = True
        else:
            ligado = False

    def desligar(self, chave, ligado):
        if(chave == False):
            ligado = False

    