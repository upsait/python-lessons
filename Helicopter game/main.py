#🌲🌳🔥🏆🌊⬜️⚡🏥🏪🚁❤️🛢️🟩

# -*- coding: utf-8 -*-
from map import Map
import time
import os
import subprocess as sp
from helicopter import Helicopter as Helico
from pynput import keyboard
from clouds import Clouds
import json

TICK_SLEEP = 0.1
TIME_UPDATE = 50
FIRE_UPDATE = 100
CLOUDS_UPDATE = 100
MAP_W, MAP_H = 40, 10 
tick = 1

field = Map(MAP_W, MAP_H)

helico = Helico(MAP_W, MAP_H)
clouds = Clouds(MAP_W, MAP_H)
field.print_map(helico)

MOVES = {'w': (-1,0), 'd':(0,1), 's': (1,0), 'a': (0,-1)  }

def process_key(key):
    print(key)
    global helico, tick, clouds, field
    c = key.char.lower()
    if c in MOVES.keys():
        dx, dy = MOVES[c][0], MOVES[c][1]
        helico.move(dx, dy)
        field.process_helicopter(helico)#перенес сюда чтобы одно посещение магазина ровнялось одной покупке
    # f - сохранение, G - востановление
    elif c == 'f':
        data = {"helicopter": helico.export_data(), 
                "clouds": clouds.export_data(), 
                "field": field.export_data(),"tick": tick}
        with open("level.json", "w") as lvl:
            json.dump(data, lvl)
    elif c=="g":
        with open("level.json", "r") as lvl:
            data = json.load(lvl)
            os.system("cls")
            helico.import_data(data["helicopter"])
            clouds.import_data(data["clouds"])
            field.import_data(data["field"])
            tick = data["tick"] or 1
                    


listener = keyboard.Listener(
    on_press=None,
    on_release=process_key)
listener.start()





while True:
    os.system("cls")#clear для маssкa
    helico.print_stats()
    field.print_map(helico)
    field.process_helicopter_life(helico)
    print("TICK ", tick)
    tick += 1
    time.sleep(TICK_SLEEP)
    if (tick % TIME_UPDATE == 0):
        field.generate_tree()
    if (tick % FIRE_UPDATE == 0):
        field.update_fires()
    if (tick % CLOUDS_UPDATE == 0):
        field.clouds.update_clouds()

