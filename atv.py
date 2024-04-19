class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    
    def frear(self):
        print(f"{self.marca} {self.modelo} freiou")
    
    def acelerar(self):
        print(f"{self.marca} {self.modelo} acelerou")

class Carro(Veiculo):
    def __init__(self, marca, modelo, cor):
        super().__init__(marca, modelo)
        self.cor = cor
    
    def abrir_porta(self):
        print(f"{self.marca} {self.modelo} porta aberta")   

class Moto(Veiculo):
    def __init__(self, marca, modelo, cilindrada):
        super().__init__(marca, modelo)    
        self.cilindrada = cilindrada
    
    def empinar(self):
        print(f"{self.marca} {self.modelo} empinou e morreu")

if __name__ == '__main__':
    carro1 = Carro("Porsche", "Gt4-RS", "Preto")   
    print(carro1.marca, carro1.modelo)
    carro1.abrir_porta()
    
    moto1 = Moto("Honda", "XRE-300", "300cc")
    print(moto1.marca, moto1.modelo, moto1.cilindrada)
    moto1.empinar()
