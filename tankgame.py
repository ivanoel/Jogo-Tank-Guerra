#!/usr/bin/python3
# __autor__ == __Ivanoel__
# Jogo de Tank

from tank import Tank
# ou import Tank da no msm, pega tudo da classe Tank.

# Aqui vc pode adicionar mais jogadores.
tanks = {"a":Tank("Rodrigo"), "b":Tank("Danilo"), "c":Tank("Thamar"), "d":Tank("Ivanoel")}

alive_tanks = len(tanks)

while alive_tanks > 1:
    
    for tank_name in sorted( tanks.keys() ):
        print(tank_name, tanks[tank_name])
        
    primeiro = input("Quem lança o projeto? ").lower()
    segundo = input("Quem leva o ataque? ").lower()

    try:
        primeiro_tank = tanks[primeiro]
        segundo_tank = tanks[segundo]
        
    except KeyError as name:
        print("Não existe esse tank!", name)
        continue
    
    if not primeiro_tank.alive or not segundo_tank.alive:
        print("Primeiro of those tanks eh morto!")
        continue
    
    print("*" * 30)

    primeiro_tank.fire_at(segundo_tank)

    if not segundo_tank.alive:
        alive_tanks -= 1

    print("*" * 30)

    for tank in tanks.values():
        if tank.alive:
            print(tank.name, "eh o ganhador!")
            break
    
              
