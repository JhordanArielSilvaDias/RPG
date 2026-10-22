from random import randint
import random
from monsters import *
def run():
    chance = randint(1, 10)
    if chance > 6:
        return False
    else:
        return True
def atk(a, b):
    rage = randint(a.atk-10, a.atk+10)
    b.hp -= rage
    return rage
def play(hero):
    r = str(input('''
[1]Explorar   [2]Ver inventario
    ''')).strip()
    if r == '1':
        explr(hero)
    elif r == '2':
        ver_invent(hero)
def explr(hero):
    chance = randint(1, 100)
    if chance in range(1, 51):
        print('Apenas pedras por aqui')
    elif chance in range(51, 76):
        itens = [Couro, Veneno, Dente, Potion, Fruit]
        item = random.choice(itens)()
        print(f'{hero.name} encontou {item}')
        resp = str(input('[1]Pegar [2]Deixar '))
        if resp == '1':
            hero.adc(item)
            ver_invent(hero)
    elif chance >75:
        print('um monstro apareceu')
        chance = randint (1, 101)
        if chance in range(71, 95):
            monster = Ogro()
        elif chance in range(41, 71):
            monster = Goblin()
        elif chance in range(95, 101):
            monster = Dragao()
        elif chance in range(1, 41):
            monster = Aranha()
        fight(hero, monster)
def usar_pocao(hero):
    if hero.invent['Poção'] > 0:
        hero.hp += 60
        if hero.hp > hero.maxhp:
            hero.hp = hero.maxhp
        hero.invent['Poção'] -= 1
        print(f'{hero.name} usou poção...')
        print(f'A vida de {hero.name} subiu para {hero.hp}')
    elif hero.invent['Poção'] == 0:
        print('não há poção para usar')
def usar_fruta(hero):
    hero.maxhp += 20
    hero.invent['Fruta'] -= 1
    print(f'{hero.name} comeu Fruta...')
    print(f'A vida maxima de {hero.name} saiu de {hero.maxhp - 20 } para {hero.maxhp}')
def drop(monster, hero):
    print(f'{monster.name} derrubou um {monster.item}')
    resp = str(input('[1]Pegar [2]Deixar '))
    if resp == '1':
        hero.adc(monster.item)
        ver_invent(hero)
def fight(hero, monster):
    print(f'Um {monster.name} surgiu das trevas!')
    while True:
        resp = str(input('''
    [1]ATACAR      [2]FUGIR
    [3]POÇÃO       [4]ITEM\n'''))
        if resp == '1':
            rage = atk(hero, monster)
            if monster.hp > 0 and hero.hp >0:
                print(f'''{hero.name} atacou, dando {rage} de dano!          
{hero.name}: {hero.hp}/{hero.maxhp}
{monster.name}: {monster.hp}/{monster.maxhp}''')
            rage = atk(monster, hero)
            if monster.hp > 0 and hero.hp > 0:
                print(f'''{monster.name} atacou {hero.name}, tirando {rage} de sua vida          
{hero.name}: {hero.hp}/{hero.maxhp}
{monster.name}: {monster.hp}/{monster.maxhp}\n''')
            elif monster.hp <= 0:
                hero.xp += monster.xp
                print(f'{hero.name} derrotou {monster.s} {monster.name} e ganhou {monster.xp} de XP.')
                print(f'ficando com {hero.xp} de XP')
                drop(monster, hero)
                if hero.xp >= hero.next_level:
                    hero.level += 1
                    print(f'Voce passou do Level {hero.level - 1} para o level {hero.level}')
                    nextlevel = hero.next_level * 2
                    print(f'Agora são necessarios {nextlevel} pontos para passar de level')
                break
            elif hero.hp <= 0:
                print(f'{hero.name} teve as entranhas devoradas pel{monster.s} {monster.name}.')
                break
        if resp == '2':
            if not run():
                print(f'{hero.name} tentou fugir, mas {monster.s} {monster.name} o encurralou\n')
                rage = atk(monster, hero)
                if monster.hp > 0 and hero.hp > 0:
                    print(f'''{monster.name} atacou {hero.name}, tirando {rage} de sua vida          
{hero.name}: {hero.hp}/{hero.maxhp}
{monster.name}: {monster.hp}/{monster.maxhp}\n''')
                continue
            else:
                print(f'{hero.name} consegue fugir')
                break
        if resp == '3':
            usar_pocao(hero)
def ver_invent(hero):
    print('-' * 30)
    print('INVENTARIO\n\n')
    for i, k in hero.invent.items():
        print(f'{i}: {k}')
    print('-' * 30)

