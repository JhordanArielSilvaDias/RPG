from act import *
from hero import *
hero = Hero('Jhordan')
while True:
    play(hero)
    if hero.hp <= 0:
        break
