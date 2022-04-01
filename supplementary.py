import os
import sys


def file_list_create(folder):
    f_list = {}
    number = 0
    for item in os.listdir(path=folder):
        number += 1
        f_list[number] = item
    return f_list


first_path = os.getcwd()

while first_path:
    file_list_first = file_list_create(first_path)
    n = len(file_list_first)
    print('Вы находитесь в папке: {}'.format(os.getcwd()))
    if n == 0:
        print('Эта папка пустая')
    else:
        for key, val in file_list_first.items():
            if os.path.isdir(file_list_first[key]):
                print('{} - [{}]'.format(key, val))
            else:
                print('{} - {}'.format(key, val))
    print('0 - Переход на уровень выше')
    print('-1 - Выход из программы')
    # print('999 - Самостоятельный ввод пути')

    try:
        second_path_number = int(input('Выберите папку/файл по номеру: '))
    except ValueError:
        print('Вы ввели текст. Введите цифрой один из указанных номеров.\n')
        first_path = os.getcwd()
    else:
        if second_path_number < 0:
            print('Выход из программы')
            sys.exit(13)
        elif second_path_number == 0:
            os.chdir('..')
            first_path = os.getcwd()
        elif second_path_number > n and second_path_number != 999:
            print('Вы ввели неверный номер. Выберите один из указанных номеров.\n')
            first_path = os.getcwd()
        elif second_path_number == 999:
            input_path = input('Введите путь: ')
            while not input_path:
                print('Необходимо ввести путь.')
                input_path = input('Введите путь: ')
            else:
                os.chdir(input_path)
                first_path = input_path
        elif os.path.isdir(file_list_first[second_path_number]):
            first_path = os.path.join(os.getcwd(), file_list_first[second_path_number])
            try:
                os.chdir(first_path)
            except PermissionError:
                print('Отказано в доступе к папке [{}]\n'.format(file_list_first[second_path_number]))
                first_path = 'D:'
            else:
                first_path = os.getcwd()
        else:
            print('Вы выбрали файл {}'.format(file_list_first[second_path_number]))
            print(' 1 - Удалить\n', '2 - Переименовать\n', '3 - Отмена\n')
            file_op_number = int(input('Выберите действие по номеру: '))
            if file_op_number == 1:
                print('Вы собираетесь удалить файл {}'.format(file_list_first[second_path_number]))
                del_choice = int(input('Вы уверены? 1 - Да, 2 - Нет \n'))
                if del_choice == 1:
                    os.remove(file_list_first[second_path_number])
                    print('Файл удален')
                    first_path = os.getcwd()
                else:
                    first_path = os.getcwd()
            elif file_op_number == 2:
                print('Вы собираетесь переименовать файл {}'.format(file_list_first[second_path_number]))
                new_name = input('Введите новое имя файла: ')
                os.rename(file_list_first[second_path_number], new_name)
                print('Имя файла изменено')
                first_path = os.getcwd()
            else:
                first_path = os.getcwd()
print('end')
