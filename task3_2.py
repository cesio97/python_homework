#В файле находятся названия фруктов. Выведите все фрукты, названия которых начинаются на заданную букву.
#а –> абрикос, авокадо, апельсин, айва.

letterFr = input('Введите букву: ')

path = 'frukt.txt'
data = open(path, mode= 'r')
for line in data:
    if letterFr == line[0]:
        print(line)
data.close()