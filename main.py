import sys
from core import create_file, create_folder, get_list, delete_file, copy_file, save_info, change_dir, game_guess_number, game_guess_human_number

save_info('Старт')

try:
    command = sys.argv[1]
except IndexError:
    print('Введите комманду. Список  команд - help')
else:
    if command == 'list':
        get_list()
    elif command == 'create_file':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла')
        else:
            create_file(name)
    elif command == 'create_folder':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название папки')
        else:
            create_folder(name)
    elif command == 'delete':
        try:
            name = sys.argv[2]
        except IndexError:
            print('Отсутствует название файла или папки')
        else:
            delete_file(name)
    elif command == 'copy':
        try:
            name = sys.argv[2]
            new_name = sys.argv[3]
        except IndexError:
            print('Отсутствует название файла или новое называние файла')
        else:
            copy_file(name, new_name)
    elif command == 'path_change':
        try:
            new_path = sys.argv[2]
        except IndexError:
            print('Отсутствует новая рабочая директория')
        else:
            change_dir(new_path)
    elif command == 'game1':
        game_guess_number()
    elif command == 'game2':
        game_guess_human_number()
    elif command == 'help':
        print('list - список файлов и папок')
        print('create_file - создание файла')
        print('create_folder - создание папки')
        print('delete - удаление файла или папки')
        print('copy - копирование файла или папки')
        print('path_change - изменение текущей рабочей директории')
        print('game1 - игра Guess_number')
        print('game2 - игра Guess_human_number')
    save_info('Конец')
