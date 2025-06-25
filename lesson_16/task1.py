# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# ●	top_up(X) - пополнить на X
# ●	count_1000() - выводит сколько целых тысяч осталось в кассе
# ●	take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег
class cassa(object):
    summ = 1000
    def top_up(self, x):
        self.summ += int(x)
    def count_1000(self):
        return self.summ//1000
    def take_away(self, x):
        ost = self.summ - int(x)
        if ost >= 0:
            return print(f"В кассе осталось {ost} рублей")
        return print(f"Ошибка. В кассе недостаточно денег")
    
cass = cassa()
print(f"сейчас в кассе - {cass.summ} рублей")
cass.top_up(input("Внесите сумму в кассу - "))
print(f"в кассе осталось {cass.count_1000()} целых тысяч")
cass.take_away(input("Забрать из кассы "))