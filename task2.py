#Задача 2. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
#A (3,6); B (2,1) -> 5,09
#A (7,-5); B (1,-1) -> 7,21

firstnum1x = int(input('Введите X первой точки = '))
firstnum1y = int(input('Введите Y первой точки = '))
secondnum2x = int(input('Введите X второй точки = '))
secondnum2y= int(input('Введите Y второй точки = '))

distance = ((secondnum2x - firstnum1x) ** 2 + (secondnum2y - firstnum1y) ** 2) ** (0.5)
print(round (distance, 2))