import time
def fight(hero, monster):
    while True:
        monster.hp -= hero.damege
        print(f'{hero.nome} atacou, tirando {hero.damege} pontos de vida do {monster.nome}')
        if monster.hp < 1:
            monster.hp = 0
            print(f'''
{hero.nome}: {hero.hp}/{hero.mxhp}
{monster.nome}: {monster.hp}/{monster.mxhp}
            ''')
            time.sleep(2)
            break
        print(f'''
{hero.nome}: {hero.hp}/{hero.mxhp}
{monster.nome}: {monster.hp}/{monster.mxhp}
        ''')
        time.sleep(2)
        hero.hp -= monster.damege
        print(f'{monster.nome} atacou, tirando {monster.damege} pontos de vida do {hero.nome}')
        if hero.hp < 1:
            hero.hp = 0
            print(f'''
{hero.nome}: {hero.hp}/{hero.mxhp}
{monster.nome}: {monster.hp}/{monster.mxhp}
            ''')
            time.sleep(2)
            break
        print(f'''
{hero.nome}: {hero.hp}/{hero.mxhp}
{monster.nome}: {monster.hp}/{monster.mxhp}
        ''')
        time.sleep(2)
    if hero.hp > 1:
        print(f'{hero.nome} derrotou {monster.nome}')
    if monster.hp > 1:
        print(f'{monster.nome} derrotou {hero.nome}')