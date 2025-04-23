from models import Pokemon, Tipos
from data import todos_os_pokemons, meus_pokemons

def cadastrar_pokemon():
    nome = ""
    vida = 0
    ataque = 0
    tipo = Tipos.FOGO
    while True:
        nome = input("Nome: ")
        if(len(nome)<10):
            break
        else:
            print("Nome não deve ultrapassar 10 caracteres.")
    
    while True:
        try:
            vida = int(input("Vida: "))
            break
        except:
            print("Entrada inválida.")
    
    while True:
        try:
            ataque = int(input("Ataque: "))
            break
        except:
            print("Entrada inválida.")

    while True:
        print("Escolha o tipo:\n1- Fogo\n2- Agua\n3- Planta")
        try:
            escolha = int(input("Tipo: "))
            if(escolha==1): 
                tipo = Tipos.FOGO
                break
            elif(escolha==2):
                tipo = Tipos.AGUA
                break
            elif(escolha==3):
                tipo = Tipos.PLANTA
                break
            else:
                print("Entrada inválida.")
        except:
            print("Entrada inválida.")
    
    todos_os_pokemons.append(Pokemon(nome,vida,ataque,tipo,0))

def capturar_pokemon():
    print("Escolha um pokémon para capturar:")
    for i in range(len(todos_os_pokemons)):
        print(f"{i+1}-",todos_os_pokemons[i].nome)
    
    while True:
        escolha = int(input())
        if 1 <= escolha <= len(todos_os_pokemons):
            p = todos_os_pokemons[escolha-1]
            meus_pokemons.append(Pokemon(p.nome, p.vida, p.ataque, p.tipo, p.nivel))
            break
        else:
            print("Entrada inválida.")

def exibir_pokemon():
    if not meus_pokemons:
        print("Você não tem pokémons.")
        return
    print("Lista de pokémons:")
    for p in meus_pokemons:
        print(f"{p.nome}, nível: {p.nivel}")

def reviver_pokemon():
    if(not meus_pokemons):
        print("Você não tem pokemons.")
        return []
    print("Selecione o pokémon para reviver:")
    for i in range(len(meus_pokemons)):
        print(f"{i+1}-",meus_pokemons[i].nome)
    
    while True:
        escolha = int(input())
        if 1 <= escolha <= len(meus_pokemons):
            meus_pokemons[escolha - 1].reviver()
            break
        else:
            print("Entrada inválida.")

def tipoString(tipo:Tipos):
    if(tipo == Tipos.FOGO):
        return "Fogo"
    elif(tipo == Tipos.AGUA):
        return "Agua"
    else:
        return "Planta"