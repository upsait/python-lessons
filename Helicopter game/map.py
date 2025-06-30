# -*- coding: utf-8 -*-
# 0 - поле
# 1 - дерево
# 2 - река
# 3 - госпиталь
# 4 - магазин
# 5 - огонь
from utils import randbool
from utils import rendcell
from utils import rendcell2
from clouds import Clouds
from utils import game_over

CELL_TYPSE = "🟩🌳🌊🏥🏪🔥🚁"
TREE_BONUS = 100
UPGRADE_COST = 500
LIFE_COST = 1000

class Map(object):
    def __init__(self, w, h):
        self.cells = [[0 for i in range(w)] for i in range(h)]
        self.w = w
        self.h = h 
        self.generate_forest(70,100)
        self.generate_river(50)
        self.generate_river(50)
        self.generate_upgrade_shop()
        self.generate_hospital()
        self.clouds = Clouds(w, h)



    def print_map(self, helico):
        print("⬛"*(self.w + 2))
        for ri in range(self.h):
            print("⬛", end="")
            for ci in range(self.w):
                cell = self.cells[ri][ci]
                if (self.clouds.cells[ri][ci] == 1):
                    print("⬜️", end="")
                elif (self.clouds.cells[ri][ci] == 2):
                    print("⚡", end="")
                elif(helico.x == ri and helico.y == ci):
                    print("🚁", end="")
                    
                elif cell >= 0 and cell < len(CELL_TYPSE):
                    print(CELL_TYPSE[cell], end="")
            print("⬛")
        print("⬛"*(self.w + 2))

    def check_bounds(self, x, y):
        if(x<0 or y<0 or x >= self.h or y >= self.w):
            return False
        return True
    
#проверка есть ли вода с боков
    def cell_check(self, x, y, x2, y2):
        def check_true(ctx, cty):
            if self.check_bounds(ctx, cty):
                if self.cells[ctx][cty] == 2 and (ctx,cty) != (x,y):
                    return True
                return False
        if (check_true(x2-1, y2)) or (check_true(x2+1, y2)) or (check_true(x2, y2+1)) or (check_true(x2, y2-1)):
            return False
        return True

        
    def generate_forest(self, r, mxr):
        for rx in range(self.h):
            for ry in range(self.w):
                if randbool(r, mxr):
                    self.cells[rx][ry] = 1



    def generate_river(self, l):
        rc = rendcell(self.h, self.w)
        rx, ry = rc[0],rc[1]
        self.cells[rx][ry] = 2
        n = 0
        while l > 0:
            rc2 = rendcell2(rx, ry)
            rx2, ry2 = rc2[0], rc2[1]
            if (self.check_bounds(rx2, ry2) and self.cell_check(rx, ry, rx2, ry2)):
                self.cells[rx2][ry2] = 2
                rx, ry  = rx2, ry2
                l -= 1
                n = 0
            elif n<25:#если подходящих ячеек не возможно найти то выход из цикла
                n +=1
            else:
                break
    
    def generate_tree(self):
        c = rendcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 0:
            self.cells[cx][cy] = 1
    
    def generate_upgrade_shop(self):
        c = rendcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] != 2:
            self.cells[cx][cy] = 4
        else:
            self.generate_upgrade_shop()
    
    def generate_hospital(self):
        c = rendcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] != 2 and self.cells[cx][cy] != 4:
            self.cells[cx][cy] = 3
        else:
            self.generate_hospital()
    
    def generate_fire(self):
        c = rendcell(self.h, self.w)
        cx, cy = c[0], c[1]
        if self.check_bounds(cx, cy) and self.cells[cx][cy] == 1:
            self.cells[cx][cy] = 5


    def update_fires(self):
            for rx in range(self.h):
                for ry in range(self.w):
                    if self.cells[rx][ry] == 5:
                        self.cells[rx][ry] = 0
            for i in range(10):
                self.generate_fire()
    
    def process_helicopter(self, helico):
        c = self.cells[helico.x][helico.y]
        if(c == 2):
            helico.tank = helico.mxtank
        elif(c == 5 and helico.tank > 0):
            self.cells[helico.x][helico.y] = 1
            helico.tank -= 1
            helico.score += TREE_BONUS
        elif(c == 4 and helico.score >= UPGRADE_COST):
            helico.score -= UPGRADE_COST
            helico.mxtank += 1
        elif(c == 3 and helico.score >= LIFE_COST):
            helico.score -= LIFE_COST
            helico.lives += 10

    def process_helicopter_life(self, helico):
        g = self.clouds.cells[helico.x][helico.y]
        if(g == 2):
            helico.lives -= 1
            if(helico.lives == 0):
                game_over(helico)


    def export_data(self):
        return {"cells": self.cells}
    
    def import_data(self, data):
        self.cells = data["cells"] 