# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

n = int(input('Введите число: '))
list = list(range(-n, n+1))
for i in 1, 2:
    list.insert(0, list[len(list)-1])
    del list[len(list)-1]
print(list)