def fight(hero, monster):
    while hero.hp > 0:
        monster.hp -= hero.damege
        print(f'{hero.nome} atacou, tirando {hero.damege} pontos de vida do {monster.nome}')
        hero.hp -= monster.damege
        print(f'{monster.nome} atacou, tirando {monster.damege} pontos de vida do {hero.nome}')
        print(f'''
{hero.nome}: {hero.hp}
{monster.nome}: {monster.hp}
''')
    if hero.hp > 0:
        print(f'{hero.nome} derrotou {monster.nome}')
    if monster.hp > 0:
        print(f'{monster.nome} derrotou {hero.nome}')