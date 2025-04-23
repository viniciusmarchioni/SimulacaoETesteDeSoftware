from models import *
from data import *

def ataque_pokemon(p1:Pokemon,p2:Pokemon):
    if(p1.tipo == Tipos.AGUA and p2.tipo == Tipos.FOGO):
        p2.vida_atual-=p1.ataque*2
    elif(p1.tipo == Tipos.PLANTA and p2.tipo == Tipos.AGUA):
        p2.vida_atual-=p1.ataque*2
    elif(p1.tipo == Tipos.FOGO and p2.tipo == Tipos.PLANTA):
        p2.vida_atual-=p1.ataque*2
    else:
        p2.vida_atual-=p1.ataque

def historico_de_batalha():
    if(not historico_de_batalhas):
        print("Você nunca batalhou.")
        return
    
    for i in historico_de_batalhas:
        print(f'{i["Pokemon-jogador"]} X {i["Pokemon-adversario"]}, {"Vitória" if i["resultado"] == 0 else "Derrota"}')

def batalha(pj:Pokemon,pa:Pokemon):
    global qtd_batalhas
    turno = True
    qtd_batalhas+=1
    while pj.vida_atual > 0 and pa.vida_atual > 0:
        if(turno):
            ataque_pokemon(pj,pa)
            turno = False
        else:
            ataque_pokemon(pa,pj)
            turno = True
    if(pj.vida_atual > 0):
        print("Jogador venceu!")
        historico_de_batalhas.insert(0,{
            "Pokemon-jogador":pj.nome,
            "Pokemon-adversario":pa.nome,
            "resultado":0,
            "id_batalha":qtd_batalhas

        })
    else:
        print("Jogador perdeu!")
        historico_de_batalhas.insert(0,{
            "Pokemon-jogador":pj.nome,
            "Pokemon-adversario":pa.nome,
            "resultado":1,
            "id_batalha":qtd_batalhas
        })
