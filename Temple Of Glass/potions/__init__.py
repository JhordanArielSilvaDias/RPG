class Item:
    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return self.nome
class Couro(Item):
    def __init__(self):
        super().__init__("Couro")
class Veneno(Item):
    def __init__(self):
        super().__init__("Veneno de Aranha")
class Dente(Item):
    def __init__(self):
        super().__init__("Dente de Gobin")
class Potion(Item):
    def __init__(self):
        super().__init__("Poção")
        self.cura = 60
class Fruit(Item):
    def __init__(self):
        super().__init__("Fruta")