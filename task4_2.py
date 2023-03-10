# В первой строке файла находится информация об ассортименте мороженного, во второй - информация о том, какое мороженное есть на складе. Выведите названия того товара, который закончился.
# Пример: 1 строка файла. «Сливочное», «Бурёнка», «Вафелька», «Сладкоежка» 2 строка файла. «Сливочное», «Вафелька», «Сладкоежка»
# Ответ. Закончилось: «Бурёнка»

""" data = open('ice-cream.txt', mode= 'w', encoding='utf8')
data.write('«Сливочное», «Бурёнка», «Вафелька», «Сладкоежка»\n«Сливочное», «Вафелька», «Сладкоежка»')
data.close() """

with open('ice-cream.txt', mode='r', encoding='utf8') as unknown:
    assortment = set(unknown.readline().rstrip().split(', '))
    current = set(unknown.readline().rstrip().split(', '))
    print(f'Закончилось:', *assortment - current)