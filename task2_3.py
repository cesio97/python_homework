# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

str1 = input('Введите первую строку: ')
str2 = input('Введите вторую строку: ')
countChar = 0

for i in str1:
    for j in str2:
        if j == i:
            countChar += 1
    print(f'{i} - {countChar}')
    countChar = 0


