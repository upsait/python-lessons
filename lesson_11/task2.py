# Задание №2
#ТЕКСТ ЗАДАНИЯ НИЖЕ
import collections
pets = {
    1:
        {
            "Мухтар": {
                "Вид питомца": "Собака",
                "Возраст питомца": 9,
                "Имя владельца": "Павел"
            },
        },
    2:
        {
            "Каа": {
                "Вид питомца": "желторотый питон",
                "Возраст питомца": 19,
                "Имя владельца": "Саша"
            },
        },
}
def vozr(id, n):
        voz = input("Возраст питомца цифрами ")
        if voz.isdigit():
            voz = int(voz)
            if voz > 49:
                print("Укажет возраст меньше 49 лет ")
                vozr(id, n)
            else:
                pets[id][n]["Возраст питомца"] = int(voz)
        else:
            vozr(id, n)
def modification(id):
    n = input("Введите имя питомца ")
    if n == "exit":
        programm()
    else:
        pets[id] = {}
        pets[id][n] = {}
        vid = input("Вид питомца ")
        pets[id][n]["Вид питомца"] = vid
        vozr(id,n)
        name = input("Имя владельца ")
        pets[id][n]["Имя владельца"] = name
def create():
    last = collections.deque(pets, maxlen=1)[0]
    modification(last+1)
def get_suffix(age):
            god = [1,21,31,41]
            goda = [2,3,4,22,23,24,32,33,34,42,43,44]
            let = [25,26,27,28,29,30,35,36,37,38,39,40,45,46,47,48,49]   
            if age in god:
                yer = f"{age} год"
            elif age in goda:
                yer = f"{age} года"
            elif age in let or 5 <= age <=20:
                yer = f"{age} лет"
            return yer
def get_pet(id): #проверяем есть ли такой id
    if id.isdigit():
        id = int(id)
        if id >= 1:
            if id in pets.keys():
                return True
    return False

def pets_list(id): #получить весь словарь
    if id == "all":
        for id in pets.keys():
            for name in pets[id].keys():
                print(f"ID - {id} Это {pets[id][name]["Вид питомца"]} по кличке \"{name}\". Возраст питомца: {get_suffix(pets[id][name]["Возраст питомца"]):}. Имя владельца: {pets[id][name]["Имя владельца"]}")
    else:
            for name in pets[id].keys():
                print(f"ID - {id} Это {pets[id][name]["Вид питомца"]} по кличке \"{name}\". Возраст питомца: {get_suffix(pets[id][name]["Возраст питомца"]):}. Имя владельца: {pets[id][name]["Имя владельца"]}")
def read(): #чтение из словаря pets по id
    id = input("Введите id питомца (или all чтобы получить информацию о всех питомцах сразу) - ")
    if id == "all":
        pets_list('all')
    elif id == "exit":
        programm()
    else:
        get_pet(id)
        if get_pet(id) == True:
            pets_list(int(id))
        else:
             print("Такого id нет, попробуйте еще")
def update():
    id = input("Введите id питомца чтобы обновить о нем информацию - ")
    if id == "exit":
        programm()
    else:
        get_pet(id)
        if get_pet(id) == True:
           modification(int(id))
           print(f"Запись с id {id} - успешно обновлена")
           programm()
        else:
             print("Такого id нет, попробуйте еще")
def delete():
    id = input("Введите id питомца чтобы удалить запись из базы - ")
    if id == "exit":
        programm()
    else:
        get_pet(id)
        if get_pet(id) == True:
           pets.pop(int(id))
           print(f"Запись с id {id} - успешно удалена")
           programm()
        else:
             print("Такого id нет, попробуйте еще")
def programm():
    command = input("Введите команду - ")
    while command != 'stop':
        if command == 'create':
            create()
        elif command == 'read': 
            read()
        elif command == 'update':
             update()
        elif command == 'delete': 
            delete()
        else:
            command = input("Есть только команды.(stop; create; read; update; delete) Введите команду - ")
programm()#запуск всей программы


# В Урок №10. Задание №1 вы создавали словарь с информацией о питомце. Теперь нам нужна "настоящая" база данных для ветеринарной клиники.
# Подробный требуемый функционал будет ниже. Пока что справка:
# ●	Создайте функцию create
# ●	Создайте функцию read
# ●	Создайте функцию update
# ●	Создайте функцию delete
# ●	Используйте словарь pets, который будет предоставлен ниже, либо создайте свой аналогичный
# Функция create:
# Данная функция будет создавать новую запись с информацией о питомце и добавлять эту информацию в наш словарь pets
# Функция read
# Данная функция будет отображать информацию о запрашиваемом питомце в виде: 
# Это желторотый питон по кличке "Каа". Возраст питомца: 19 лет. Имя владельца: Саша
# Функция update
# Данная функция будет обновлять информацию об указанном питомце
# Функция delete
# Данная функция будет удалять запись о существующем питомце
# ________________________________________
# Структруа результирующего словаря pets будет как и в Урок №10. Задание №1, но с небольшим видоизменением: 
# Словарь pets
# pets = {
#     1:
#         {
#             "Мухтар": {
#                 "Вид питомца": "Собака",
#                 "Возраст питомца": 9,
#                 "Имя владельца": "Павел"
#             },
#         },
#     2:
#         {
#             "Каа": {
#                 "Вид питомца": "желторотый питон",
#                 "Возраст питомца": 19,
#                 "Имя владельца": "Саша"
#             },
#         },
#     # и так далее
# }
# Здесь, 1 и 2 - это идентификаторы наших питомцев. Это уникальные ключи, по которым мы сможем обращаться к нашим записям в "базе данных"
# Суть будущей программы будет заключаться в следующем:
# ●	Программа будет работать с помощью цикла while с условием command != 'stop', то есть до тех пор, 
# пока на предложение ввести команду, пользователь не введёт слово stop
# ●	Перед взаимодействием с "базой данных" запрашивается одна из команд в качестве пользовательского ввода. 
# Пусть это будет переменная command
# ●	Функция create должна добавлять новую информацию таким образом, чтобы идентификатор увеличивался на единицу. 
# Чтобы у вас была возможность получать последний ключ в словаре воспользуйтесь импортом модуля collections. 
# В начале вашей программы пропишите строчку: import collection, а в функции create в первых строках пропишите следующий код: 

# def create():
#   last = collections.deque(pets, maxlen=1)[0]
# last в данном случае и будет число последнего ключа (или в нашей логике - идентификатора записи). 
# Именно его и необходимо будет увеличивать на единицу при добавлении следующей записи.
# Как вам уже известно - суть функций заключается в том, чтобы использовать один и тот же код в нескольких местах. 
# В данной задаче вам предстоит получать информацию о питомце несколько раз. Чтобы не повторяться в коде, вам нужно создать такие функции 
# get_pet(ID):
# def get_pet(ID):
#   # функция, с помощью которой вы получите информацию о питомце в виде словаря
#   # сделайте проверку, если питомца с таким ID нету в нашей "базе данных"
#   # верните в этом случае False
#   # а если питомец всё же есть в "базе данных" - верните информацию о нём
#   # выглядеть это может примерно так:
#   return pets[ID] if ID in pets.keys() else False
# get_suffix(age):
# def get_suffix(age):
#   # функция, с помощью которой можно получить суффикс
#   # 'год', 'года', 'лет'
#   # реализацию этой функции вам предстоит придумать самостоятельно
#   # функция будет возвращать соответствующую строку
#   return
# pets_list():
# def pets_list():
#   # Эта функция будет создана для удобства отображения всего списка питомцев
#   # Информацию по каждому питомцу можно вывести с помощью цикла for
# Обратите внимание, если ID не существует в словаре с питомцами - будет возникать ошибка. Вам можно от неё избавиться, если правильно составить проверочное условие. Здесь не потребуется использовать такие конструкции, как try, except, чтобы обработать возникшую ошибку

