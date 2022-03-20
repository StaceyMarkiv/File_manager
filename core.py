import datetime
import os
import shutil
import sys


def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as f:
        if text:
            f.write(text)


def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Такая папка уже существует')
        # for i in range(1, 5):
        #     os.mkdir('{}_{}'.format(name, i))


def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Такая папка уже существует')
    else:
        shutil.copy(name, new_name)


def save_info(message):
    current_time = datetime.datetime.now()
    result = f'{current_time} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write(result + '\n')


def change_dir(path):
    os.chdir(path)
    print('Новая рабочая директория: {}'.format(os.getcwd()))
    # for item in os.listdir():
    #     print(item)


def game_guess_number():
    sys.path.append('D:\stasy\PycharmProjects\Guess_number')
    import guess_number


def game_guess_human_number():
    sys.path.append('D:\stasy\PycharmProjects\Guess_human_number')
    import guess_human_number


if __name__ == '__main__':
    for i in sys.path:
        print(i)
