# 1) морской бой
from random import randint

def print_matrx(arr):
    '''
    Выводит в консоль состояние поля
    '''
    for i in range(len(arr)):
        print(arr[i])

def is_number(txt):
    '''
    Проверяет явлеется ли ввод числом
    '''
    try:
        int(txt)
        return True
    except ValueError:
        print('Ввод не верный, попробуйте еще раз!')
        return False

def check_usr_input_num(prase):
    '''
    Зацикливает функцию "is_number" пока пользователь не введет число
    В аргумент prase передаем строку (приглашение для ввода)
    '''
    while True:
            input_usr = input(prase)
            check_rows =  is_number(input_usr)
            if check_rows != True:
                continue
            else:
                return int(input_usr)

def check_usr_dots(prase):
    '''
    Проверяет корректность координат выстрела введеных пользователем с изпользованием функции "check_usr_input_num" (цикличная проверка ввода на число)
    В аргумент prase передаем строку (приглашение для ввода)
    '''
    while True:
        usr_dot = check_usr_input_num(prase)
        usr_dot = usr_dot - 1
        if usr_dot < 0 or rows < usr_dot + 1:
            print('вы вышли за пределы поля, попробуйте еще раз! ')
            continue
        return usr_dot

def play_game(x1, y1, x2, y2, matrix):
    '''
    Один ход игры и вывод в консоль результат хода
    В аргументы "x1, y1" предаются выстрелы, В "x2, y2" - сохраненые координаты корабля, В matrix - чье поле сейчас печатаем
    Работает совместно с функцией "print_matrx"
    '''
    if x1 == x2 and y1 == y2:
        print('Корабль уничтожен!')
        matrix[x2][y2] = 'X'
        print_matrx(matrix)
        return -1
    elif matrix[x1][y1] == 1:
        print('Сюда уже стреляли!')
        print_matrx(matrix)
    else:
        print('Мимо!')
        matrix[x1][y1] = 1
        print_matrx(matrix)


print('Игра морской бой (Легкий режим) с компьютером')

while True:
    rows = check_usr_input_num('Введите размер квадратного поля (минимально число для квадрата 2): ')
    if rows < 2:
        print('Поле не может быть меньше 2 строк и колонок, попробуйте еще раз')
        continue
    columns = rows
    break

comp_matrix = [[0 for j in range(columns)] for i in range(rows)]
usr_matrix = [[0 for j in range(columns)] for i in range(rows)]

print_matrx(usr_matrix)
usr_ship_x = check_usr_dots('Введите номер строки куда прячем корабль: ')
usr_ship_y = check_usr_dots('Введите номер колонки куда прячем корабль: ')
print('Ваш корабль будет отображаться как символ "2"')
usr_matrix[usr_ship_x][usr_ship_y] = 2

comp_ship_x = randint(0, rows - 1)
comp_ship_y = randint(0, columns - 1)

difficl_lvl_ez = rows * columns - 1
print(f'Колличество попыток {difficl_lvl_ez}')

while difficl_lvl_ez > 0:
    print('Поле противника')
    print_matrx(comp_matrix)
    print('Ваше поле')
    print_matrx(usr_matrix)

    print('Ваш ход')
    print(f'Колличество попыток осталось {difficl_lvl_ez}')
    usr_shoot_x = check_usr_dots('Введите номер строки: ')
    usr_shoot_y = check_usr_dots('Введите номер колонки: ')

    end = play_game(usr_shoot_x, usr_shoot_y, comp_ship_x, comp_ship_y, comp_matrix)
    if end == -1:
        break
    difficl_lvl_ez -=1
   
    print('Ход копьютера')
    comp_shoot_x = randint(0, rows - 1)
    comp_shoot_y = randint(0, columns - 1)

    end = play_game(comp_shoot_x, comp_shoot_y, usr_ship_x, usr_ship_y, usr_matrix)
    if end == -1:
        break
    

if difficl_lvl_ez <=0:
    print('Попытки закончились!')