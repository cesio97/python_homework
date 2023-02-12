names = ['Иванов Иван Иванович', 'Петров Петр Петрович', 'Сидоров Сидр Иванович']
tel = ['+375293626519\n', '+375293416907\n', '+375445944228\n']


def printTelef():
    list = []
    for i in range(len(names)):
        list.append(names[i])
        list.append(tel[i])
    print(' '.join(list))


def addTelef():
    name = input("Введите ФИО: ")
    telephone = input("Введите tel: ") + '\n'

    names.append(name)
    tel.append(telephone)
    print('Данные добавлены!')

def serchTelef():
    name = input("Введите ИМЯ: ")
    for i in range(len(names)):
        if name in names[i] : print(names[i] + ' ' + tel[i])


def saveAsHTML():

    book = open('book.html', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])
        book.write('<br>')

    print('Файл "book.html" сохранен!')


def saveAsXML():

    book = open('book.xml', 'w', encoding='utf-8')
    for i in range(len(names)):
        book.write(names[i])
        book.write(' ')
        book.write(tel[i])

    print('Файл "book.xml" сохранен!')