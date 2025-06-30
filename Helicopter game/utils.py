#утилиты (функция рандома)
from random import randint as rand # импортировали из библиотеки random метод randint и обозвали rand
import os

def randbool(r, mxr):
    t = rand(0, mxr)
    return t <= r

def rendcell(h, w):
    rh = rand(0, h-1)
    rw = rand(0, w-1)
    return rh,rw

# 0 - вверх, 1 - право, 2 - низ, 3 - лево
def rendcell2(x,y):
    t = rand(0,3)
    moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    dx, dy = moves[t][0], moves[t][1]
    return (x + dx, y + dy)


def game_over(helico):
    os.system("cls")
    print("X"*50)
    print("X"," "*48)
    print(f"X             GAME OVER ваш счет {helico.score}")
    print("X"," "*48)
    print("X"*50)
    exit(0)
