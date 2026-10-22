from potions import *
class Ogro:
    def __init__(self):
        self.name = 'Ogro'
        self.hp = 80
        self.maxhp = 80
        self.atk = 15
        self.s = 'o'
        self.item = Dente()
        self.xp = 30
class Aranha:
    def __init__(self):
        self.name = 'Aranha'
        self.hp = 50
        self.maxhp = 50
        self.atk = 9
        self.s = 'a'
        self.item = Potion()
        self.xp = 15
class Goblin:
    def __init__(self):
        self.name = 'Goblin'
        self.hp = 70
        self.maxhp = 70
        self.atk = 10
        self.s = 'o'
        self.item = Potion()
        self.xp = 15
class Dragao:
    def __init__(self):
        self.name = 'Dragão'
        self.hp = 125
        self.maxhp = 125
        self.atk = 25
        self.s = 'o'
        self.item = Fruit()
        self.xp = 50
