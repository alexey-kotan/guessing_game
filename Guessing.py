from random import *

def is_valid(n): # проверка корректности введенного числа
    if n.isdigit() == True and diap.isdigit() == True and 1 <= int(n) <= int(diap):
        return True
    else:
        return False

def game():
    print('Добро пожаловать в числовую угадайку \nВ каком диапазоне от 1 до ___ вы хотите угадывать число?')
    global diap
    diap = input()
    rand = randint(1, int(diap))
    counter = 0
    while True:
        num = input(f'Введите число от 1 до {diap}:\n')
        if is_valid(num) == False:
            print(f'А может быть все-таки введем целое число от 1 до {diap}?')
        else:
            num = int(num)
            if num < rand:
                print('Ваше число меньше загаданного, попробуйте еще разок')
                counter += 1
            elif num > rand:
                print('Ваше число больше загаданного, попробуйте еще разок')
                counter += 1
            elif num == rand:
                counter += 1
                print(f'Поздравяю! Вы угадали с {counter} попытки.')
                break
    print('Хотите повторить игру? \n    1 - Да \n    2 - Нет')
    while True:
        otvet = input()
        if otvet == '2':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
        elif otvet == '1':
            game()
        else:
            print('Неверный ввод! Попробуйте еще раз.')
            continue

game()