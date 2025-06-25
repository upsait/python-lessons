# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# ●	go_up() - увеличивает y на s
# ●	go_down() - уменьшает y на s
# ●	go_left() - уменьшает x на s
# ●	go_right() - увеличивает y на s
# ●	evolve() - увеличивает s на 1
# ●	degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# ●	count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции
import math
class turtle(object):
    x = 0
    y = 0
    s = 1
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
    def go_up(self):
        self.y += self.s
    def go_down(self):
        self.y -= self.s
    def go_left(self):
        self.x -= self.s
    def go_right(self):
        self.x += self.s
    def evolve(self):
        self.s += 1
    def degrade(self):
        if self.s <= 0:
            self.s -= 1
        else:
            return print("s не может стать ≤ 0")
    def count_moves(self, x2, y2):
        x2 = int(x2)
        y2 = int(y2)
        sx = 0
        sy = 0
        if self.x != x2:
            if self.x < x2:
                for i in range(self.x, x2):
                    sx += +1
            else:
                for i in range(self.x, x2, -1):
                    sx += +1
            sx = math.ceil(sx/self.s)
        if self.y != y2:
            if self.y < y2:
                for i in range(self.y, y2):
                    sy += +1  
            else:
                for i in range(self.y, y2, -1):
                    sy += +1
            sy = math.ceil(sy/self.s)
        count = sx + sy
        return print(f"Минимальное количество действий, за которое черепашка сможет добраться до {x2}; {y2}, c шагом s={self.s}, от текущей позиции {self.x}; {self.y}, равно {count}")

h = turtle(input("введите x "), input("введите y "))
h.evolve()

h.count_moves(input("введите x конечной точки "), input("введите y конечной точки "))