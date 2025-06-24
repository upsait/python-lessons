# Задание №2
# Создайте класс Autobus, который наследуется от класса Transport. 
# Дайте аргументу Autobus.seating_capacity() значение по умолчанию 50.
# Используйте переопределение метода.
# Используйте следующий код для родительского класса транспортного средства:
# class Transport:
#    def __init__(self, name, max_speed, mileage):
#        self.name = name
#        self.max_speed = max_speed
#        self.mileage = mileage

#    def seating_capacity(self, capacity):
#        return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
# Ожидаемый результат вывода:
# Вместимость одного автобуса Renaul Logan: 50 пассажиров
class Transport(object):
   def __init__(self, name, max_speed, mileage):
       self.name = name
       self.max_speed = max_speed
       self.mileage = mileage

   def seating_capacity(self, capacity):
       return f"Вместимость одного автобуса {self.name}  {capacity} пассажиров"
class Autobus(Transport): #Создан класс Autobus!
    capacity = 50 #значение по умолчанию 50.
    def seating_capacity(self):
        return super().seating_capacity(self.capacity) #вызов родительского метода и передача ему аргумента по умолчанию 
Autobus = Autobus('Renaul Logan', 180, 12)
print(Autobus.seating_capacity())

