import json
from tabulate import tabulate
with open("library.json", 'r', encoding='utf-8') as f:
    data = json.load(f)

def hi():
    print("Введите название книги: ")
    n_b = input()
    print("Введите ФИ автора книги: ")
    n_a = input()
    return n_b, n_a

def create():
    n_b, n_a = hi()
    print("Введите имя человека, который берет книгу: ")
    n_bor = input()
    boo = False
    for key, obj in data.items():
        for it in obj:
            #if n_b in it.values() and n_a in it.values():
            if it["Title"] == n_b and it["Author"] == n_a:
                it["BorrowedBy"].append(n_bor)
                with open('library.json', 'w') as f:  #запись изменений обратно в json файл
                    json.dump(data, f, indent=4)
                boo = True
                s = n_bor + ' взял книгу "' + n_b + '"'
                print(s)
    if boo == False:
        print("Неверно введено название книги или ФИ автора")

def read():
    n_b, n_a = hi()
    boo = False
    for key, obj in data.items():
        #if isinstance(obj, dict) and n_b in obj.values():
        for it in obj:
            if it["Title"] == n_b and it["Author"] == n_a:
                print("Эту книгу брали следующие читатели: ")
                a = ', '.join(map(str, it["BorrowedBy"]))
                print(a)
                k = len(it["BorrowedBy"])
                print(k, " читателей/я/ь")
                boo = True
    if boo == False:
        print("Неверно введено название книги или ФИ автора")
def update():
    with open('library.json', 'w') as f:  # запись изменений обратно в json файл
        json.dump(data, f, indent=4)
    print("Каталог обновлён")

def deleting():
    n_b, n_a = hi()
    boo = False
    for key, obj in data.items():
        for it in obj:
            if it["Title"] == n_b and it["Author"] == n_a:
                a = ', '.join(map(str, it["BorrowedBy"]))
                print("Эту книгу брали следующие люди: ", a, "\nВведите имя читателя, который возвращает книгу")
                n_bor = input()
                it["BorrowedBy"].remove(n_bor)
                with open('library.json', 'w') as f:  #запись изменений обратно в json файл
                    json.dump(data, f, indent=4)
                boo = True
    if boo == False:
        print("Неверно введено название книги или ФИ автора")
    return 0

def popular():
    k = 0
    for key, obj in data.items():
        for it in obj:
            if len(it["BorrowedBy"]) > k:
                k = len(it["BorrowedBy"])
        for it in obj:
            if len(it["BorrowedBy"]) == k:
                print(it["Title"] + ",   автор: " + it["Author"])
        print("Количество читателей: ", k)
def no_take():
    k = 0
    for key, obj in data.items():
        for it in obj:
          if len(it["BorrowedBy"]) == 0:
            k+=1
            print(k, ') ', it["Title"] + " (автор: " + it["Author"], ")")



def find():
    while True:
        print('\nВыберите пункт(номер) меню:')
        print('1 - Поиск по автору')
        print('2 - Поиск по жанру')
        print('3 - Поиск по автору и жанру')
        print('4 - Возврат в основное меню')

        ch = int(input())
        if ch == 1:
            print("Введите ФИ автора книг: ")
            n_a = input()
            boo = False
            c = 0
            for key, obj in data.items():
                for it in obj:
                    if it["Author"] == n_a:
                        c += 1
                        if c == 1: print('Книги по запросу: автор = ', n_a, ':')
                        print(it["Title"])
                        boo = True
            if boo == False: print('Книг по запросу: автор = "', n_a, '" нет в нашей библиотеке ')
        if ch == 2:
            print("Введите жанр книг: ")
            n_g = input()
            boo = False
            c = 0
            for key, obj in data.items():
                for it in obj:
                    if it["Genre"] == n_g:
                        c += 1
                        if c == 1: print('Книги по запросу: жанр = "', n_g, '":')
                        print(it["Title"])
                        boo = True
            if boo == False: print('Книг по запросу: жанр = "', n_g, '" нет в нашей библиотеке ')
        if ch == 3:
            print("Введите ФИ автора книг: ")
            n_a = input()
            print("Введите жанр книг: ")
            n_g = input()
            boo = False
            c = 0
            for key, obj in data.items():
                for it in obj:
                    if it["Author"] == n_a and it["Genre"] == n_g:
                        c += 1
                        if c == 1: print('Книги по запросу: автор = "', n_a, '" и жанр = "', n_g, '":')
                        print(it["Title"])
                        boo = True
            if boo == False: print('Книг по запросу: автор = "', n_a, '" и жанр = "', n_g, '" нет в нашей библиотеке ')
        if ch == 4:
            return 0


def exit():
    return False


def draw():
    table_data = []
    for user_id, u_d in data.items():
        for user_data in u_d:
            table_data.append([user_data["BookID"], user_data["Title"], user_data["Author"], user_data["Genre"], user_data["Year"], len(user_data["BorrowedBy"])])
    headers = ["id", "Название книги", "Автор", "Жанр", "Год", "Кол-во читателей"]
    print(tabulate(table_data, headers, tablefmt="pretty"))

draw()
flag = True
while flag:
    print('\nВыберите пункт(номер) меню:')
    print('1 - Создать новую запись, выдать книгу')
    print('2 - Список читателей книг')
    print('3 - Обновить каталог')
    print('4 - Возврат книги')
    print('5 - Найти самую популярную книгу библиотеки')
    print('6 - Поиск книг по жанру/автору')
    print('7 - Найти книги, не были взяты из библиотеки')
    print('8 - Выйти')
    try:
        choice = int(input())
        match choice:
                case 1:
                    create()

                case 2:
                    read()

                case 3:
                    update()

                case 4:
                    deleting()

                case 5:
                    popular()
                case 6:
                    find()

                case 7:
                    no_take()

                case 8:
                    #break #не работает в некоторых компиляторах
                    flag = exit()
    except ValueError:
        print("Неправильный ввод. Пожалуйста, введите номер пункта.")



