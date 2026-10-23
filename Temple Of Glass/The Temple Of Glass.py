from act import *
from hero import *
import time
print('\n\n\n')
print('Ouço o som de gotas caindo na agua...\n')
time.sleep(1)
print('O som parece distante...\n')
time.sleep(1)
print('Esta escuro... Frio...\n')
time.sleep(1)
print('com dificuldade, me levanto, tentando lembrar... Quem sou? Onde estou?')
nome = input('Qual o meu nome? estou quase lembrando... É algo como... ')
time.sleep(1)
print(f'Ah sim... {nome}... este é o meu nome...')
print('Olho ao redor... parece uma caverna, ou algo do tipo...')
hero = Hero(nome)
while hero.hp > 0:
    play(hero)
print('\033[91mGAME OVER\033[m')