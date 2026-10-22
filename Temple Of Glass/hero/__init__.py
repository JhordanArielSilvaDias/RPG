class Hero:
    def __init__(self, name = 'Heroi' ):
        self.name = name.strip().title()
        self.hp = 100
        self.maxhp = 100
        self.atk = 15
        self.invent = {'Poção': 2}
        self.xp = 0
        self.level = 1
        self.next_level = 100
    def adc(self, item):
        if item.nome in self.invent:
            self.invent[item.nome] += 1
        else:
            self.invent[item.nome] = 1
        print(f"{self.name} pegou {item.nome}")