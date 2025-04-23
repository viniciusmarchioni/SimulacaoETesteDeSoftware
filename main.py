from models import *
from data import *
from util import *
from batalha import *
import tkinter as tk

def evoluir_pokemon():
    if(not meus_pokemons):
        print("Você não tem pokemons.")
        return []

    print("Escolha um pokémon para evoluir:")
    
    for i in range(len(meus_pokemons)):
        print(f"{i+1}- {meus_pokemons[i].nome} nível: {meus_pokemons[i].nivel}")
    
    while True:
        escolha = int(input())
        if(1<=escolha < len(meus_pokemons)+1):
            meus_pokemons[escolha-1].evoluir()
            break
        else:
            print("Entrada inválida.")

def escolha_batalha():
    if(not meus_pokemons):
        print("Você não tem pokémons para batalhar.")
        return
    
    print("Escolha seu pokémon para batalha:")

    lista_pokemon = meus_pokemons[:]


    pokemon_jogador = None
    pokemon_contra = None

    while True:  
        print("1- filtrar por vida")
        print("2- filtrar por ataque")

        for i in range(len(lista_pokemon)):
            print(f"{i+3}-",lista_pokemon[i].nome, f"nivel:{lista_pokemon[i].nivel}")
        
        escolha = int(input())
        if(escolha == 1):
            lista_pokemon.sort(key=lambda x: x.vida_atual,reverse=True)
        elif(escolha==2):
            lista_pokemon.sort(key=lambda x: x.ataque,reverse=True)
        elif 3 <= escolha <= len(lista_pokemon) + 2:
            pokemon_jogador = lista_pokemon[escolha - 3]
            print("Escolhido",pokemon_jogador.nome)
            break
        else:
            print("Escolha inválida.")


    print("Escolha o pokémon que vai batalhar contra você:")

    while True:
        for i in range(len(todos_os_pokemons)):
            print(f"{i+1}-",todos_os_pokemons[i].nome, f"nível:{todos_os_pokemons[i].nivel}")

        escolha = int(input())
        if(escolha-1 < len(todos_os_pokemons)):
            p = todos_os_pokemons[escolha-1]
            pokemon_contra = Pokemon(p.nome,p.vida,p.ataque,p.tipo,p.nivel)
            break
    
    batalha(pokemon_jogador,pokemon_contra)

    pokemon_contra.reviver()

while True:

    print('''
          MENU
    1- Capturar pokémon
    2- Exibir pokémons
    3- Cadastrar pokémon
    4- Evoluir Pokémon
    5- Reviver pokémon
    6- Batalha
    7- Meu Arsenal de pokémon
    8- Histórico de batalha
    0- Sair
        ''')
    escolha = input()
    escolha = int(escolha)
    if(escolha==1):
        capturar_pokemon()
    elif(escolha==2):
        exibir_pokemon()
    elif(escolha==3):
        cadastrar_pokemon()
    elif(escolha==4):
        evoluir_pokemon()
    elif(escolha==5):
        reviver_pokemon()
    elif(escolha==6):
        escolha_batalha()
    elif(escolha==7):
        janela = tk.Tk()
        janela.title("Meu Arsenal de Pokémons")
        janela.geometry("400x250")
        lista = tk.Listbox(janela, width=50)
        for p in meus_pokemons:
            texto = f"{p.nome:12} | Nível: {p.nivel:3} | HP: {p.vida_atual:3} | Atk: {p.ataque:3} | Tipo: {tipoString(p.tipo)}"
            lista.insert(tk.END, texto)
        lista.pack(pady=20)
        tk.Label(janela, text="Não é uma pokédex é um ARSENAL", font=("Arial", 14)).pack(pady=10)
        tk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=10)
        janela.mainloop()

    elif(escolha==8):
        historico_de_batalha()
    elif(escolha==0):
        break
    else:
        print("Escolha inválida")
