from enum import Enum

class Tipos(Enum):
    FOGO = 1
    AGUA = 2
    PLANTA = 3

class Pokemon:
    def __init__(self,nome,vida,ataque,tipo,nivel):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.tipo = tipo
        self.nivel = nivel
        self.vida_atual = vida
    
    def evoluir(self):
        self.nivel+=1
        self.ataque+=5
        self.vida+=10
        self.vida_atual=self.vida
    
    def reviver(self):
        self.vida_atual = self.vida

todos_os_pokemons = [
Pokemon("Charmander",10,6,Tipos.FOGO,0),
Pokemon("Bubasauro",12,4,Tipos.PLANTA,0),
]
