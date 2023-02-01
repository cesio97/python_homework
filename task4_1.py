# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# 60 -> 2, 2, 3, 5

n = int(input("Введите число: "))
i = 2
lst = []
while i * i <= n:
    while n % i == 0:
        lst.append(i)
        n = n / i
    i = i + 1
if n > 1:
    lst.append(int(n))
print(lst)