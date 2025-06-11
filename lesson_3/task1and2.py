#Задание №1
print("введите вид животного")
type = str(input())
print("сколько лет вашему животному?")
age = int(input())
print("какая кличка у вашего животного?")
name = str(input())
print(f"Это {type} по кличке \"{name}\" Возраст: {age} года." )#f для того чтобы вставить переменные в фигурных скобках
#Задание №2
print("Укажите этапы развития человека на латыни")
print("Введите 1. Предшественники человека")
homo_habilis = str(input())
print("Введите 2. Древнейшие люди")
homo_erectus = str(input())
print("Введите 3. Древние люди")
homo_neanderthalensis = str(input())
print("Введите 4. Современные люди")
homo_sapiens = str(input())
print(homo_habilis, homo_erectus, homo_neanderthalensis, homo_sapiens, sep="=>")