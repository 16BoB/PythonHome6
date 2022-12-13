# 1) морской бой
from random import randint

def print_matrx():
    '''
    Выводит в консоль состояние поля
    '''
    for i in range(len(matrix)):
        print(matrix[i])

def is_number(txt):
    '''
    Провверяет на корректность ввод пользователя
    Явлеется ли ввод числом
    '''
    try:
        int(txt)
        return True
    except ValueError:
        print('Ввод не верный, попробуйте еще раз!')
        return False

def check_usr_dots(prase):
    '''
    Проверяет корректность координат введеных пользователем
    '''
    while True:
            txt = input(f'Введите номер {list_prase[prase]}: ')
            check_usr = is_number(txt)
            if check_usr != True:
                print_matrx()
                continue
            txt = int(txt) - 1
            if txt < 0 or rows < txt + 1:
                print(f'Вы ввели номер {list_prase[prase]}, которого нет на поле, попробуйте еще раз! ')
                print_matrx()
                continue
            break
    return txt

list_prase = ['строки', 'колонки']


print('Игра морской бой (Легкий режим)')


while True:
        rows = input('Введите размер квадратного поля (минимально число для квадрата 2): ')
        check_rows =  is_number(rows)
        if check_rows != True:
            print('Ввод не верный, попробуйте еще раз!')
            continue
        rows = int(rows)
        if rows < 2:
            print('Поле не может быть меньше 2 строк, попробуйте еще раз')
            continue
        columns = rows
        break

matrix = [[0 for j in range(columns)] for i in range(rows)]
print_matrx()

comp_ship_x = randint(0, rows - 1)
comp_ship_y = randint(0, columns - 1)

difficl_lvl_ez = rows * columns - 1
print(f'Колличество попыток {difficl_lvl_ez}')
while difficl_lvl_ez > 0:
    usr_a = check_usr_dots(0)
    usr_b = check_usr_dots(1)

    if usr_a == comp_ship_x and usr_b == comp_ship_y:
        print('Вы виграли')
        matrix[comp_ship_x][comp_ship_y] = 'X'
        print_matrx()
        break
    elif matrix[usr_a][usr_b] == 1:
        print('Вы сюда уже стреляли!')
        print_matrx()
        difficl_lvl_ez -=1
        print(f'Колличество попыток осталось {difficl_lvl_ez}')
    else:
        print('Мимо')
        matrix[usr_a][usr_b] = 1
        print_matrx()
        difficl_lvl_ez -=1
        print(f'Колличество попыток осталось {difficl_lvl_ez}')

if difficl_lvl_ez <=0:
    print('Попытки закончились!')