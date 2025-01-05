
def check_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][1] == 'X' and area[2][0] == 'X':
        return 'X'
    if area[0][0] == '0' and area[0][1] == '0' and area[0][2] == '0':
        return '0'
    if area[1][0] == '0' and area[1][1] == '0' and area[1][2] == '0':
        return '0'
    if area[2][0] == '0' and area[2][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][0] == '0' and area[2][0] == '0':
        return '0'
    if area[0][1] == '0' and area[1][1] == '0' and area[2][1] == '0':
        return '0'
    if area[0][2] == '0' and area[1][2] == '0' and area[2][2] == '0':
        return '0'
    if area[0][0] == '0' and area[1][1] == '0' and area[2][2] == '0':
        return '0'
    if area[0][2] == '0' and area[1][1] == '0' and area[2][0] == '0':
        return '0'
    return '*'


# Создадим консольную игру крестики нолики
# Первым делом нам нужно создать игровое поле в виде вложенных списков
# 1. создаем переменную
#
#
#

# area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
# print(area)

# Далее создаем функцию для перебора переменных

# for i in area:
    # print(*i) # это уже больше похоже на поле для игры

# Нам необходимо постоянно отрисовывать поле для игры
# Поэтому загоним все сделанное ранее в отдельную функцию
def draw_area(): # Действие для отрисовки поля
    for i in area:
        print(*i)
    print() # добавляем пустой принт чтоб два поля между собой на консоли не прилипали

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print('Добро пожаловать в крестики-нолики') # Выведем приветсвие
print('----------------------------------')
# Вызываем функцию
draw_area()
# area[0][0] = 'X' # Первый ноль это первый индекс в списке, второй ноль это первый индекс подсписка
# draw_area()
# Далее создаем цикл, т.к. у нас два игрока и два значения Х и 0
# Цикл создаем на 9 повторений по числу ячеек поля

for turn in range(1, 10):
    print(f'Ход: {turn}')
    if turn % 2 == 0:
        turn_char = '0'
        print('Ходят нолики')
    else:
        turn_char = 'X'
        print('Ходят крестики')

# Дадим пользователю ввести данные
    row = int(input('Введите номер строки (1, 2, 3) ')) - 1
    column = int(input('Введите номер столбца (1, 2, 3) ')) - 1
    if area[row][column] == '*':
        area[row][column] == turn_char
    else:
        print('Ячейка уже занята, Вы пропускаете ход')
        draw_area()
        continue
    area[row][column] = turn_char # Достаю из такой то строки из такой то колонны и вставляю значение Х

    draw_area()

    if check_winner() == 'X':
        print('Победа крестиков')
        break
    if check_winner() == '0':
        print('Победа ноликов')
        break
    if check_winner() == '*' and turn == 9:
        print('Ничья')