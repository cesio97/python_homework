# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def dr(x1, x2):
    if x2 == 0:
        return x1
    else:
        return dr(x2, x1 % x2)

znam = 2
N = 12

while znam < N + 1:
    chisl = 1
    while chisl < znam:
        if dr(chisl, znam) == 1:
            print(f'{chisl} / {znam}')
        chisl += 1
    znam += 1