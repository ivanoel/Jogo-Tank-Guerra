#!/usr/bin/python3
# __autor__ == __Ivanoel__
# Jogo de Tank


# Criando a classe do jogo
class Tank(object):
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.ammo = 5
        self.armor = 100

    def __str__(self):
        if self.alive:
            # return self.name+ "("+str(self.armor)+" armor, "+str(self.ammo)+" shells)"
            return "%s (%i armadura, %i tiros)" % (self.name, self.armor, self.ammo)
        else:
            return "%s (MORTO!)" % self.name

    def fire_at(self, enemy):
        if self.ammo >= 1:
            self.ammo -= 1
            print(self.name, "lançou um projeto em", enemy.name)
            enemy.hit()
        else:
            print(self.name, "não tem mais tiros!")


    def hit(self):
        self.armor -= 20
        print(self.name, "eh o alvo!")

        if self.armor <= 0:
            self.explode()

    def explode(self):
        self.alive = False
        print(self.name, "explosão!")
        


