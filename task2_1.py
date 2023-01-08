# Напишите программу, которая принимает на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


number = int(input("Введите число: "))
fact_list = []
fact = 1
for i in range(1, number+1):
    fact *= i
    fact_list.append(fact)
print(fact_list)