#Создайте файл. Запишите в него N первых элементов последовательности Фибоначчи.
#6 –> 1 1 2 3 5 8

N = int(input('Введите число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n-1) + fib(n-2)


list = []
for a in range(1, N+1):
    list.append(fib(a))

data = open('file1.txt', mode= 'w')
data.write(str(list))
data.close()