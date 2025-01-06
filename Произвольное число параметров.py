# Создаем функцию с неизвестным числом параметров

def test_func(*params):
    print(params)

test_func()
test_func(1, 2, 3, 4)

# Допустим нам нужно посчитать аргументы, но мы не знаем сколько пользователь задаст чисел
# values - значения (параметр), summator - сумма, s - переменная
# далее создадим цикл for который будет перебирать эти значения

def summator(*values):
    s = 0
    for i in values:
        s += i
    return s
print(summator(1, 2, 3, 4))
# Мы получили сумму введенных аргументов

# Такие параметры можно комбинировать

def summator(txt, *values, type='sum'):
    s = 0
    for i in values:
        s += i
    return f'{txt}{s} {type}'
print(summator('Сумма чисел: ', 2, 3, 4))

# Так же мы можем менять параметры
print(summator('Сумма чисел: ', 2, 3, 4, type='summator'))

# Например создадим функцию которая будет собирать информацию о человеке

def info(**values):
    print('ТИП: ', type(values))
    print('Аргумент:', values)

info(name='Denis', course="Python")

# Теперь мы можем пройтись по этому словарику используя функцию for и сделать более читаемым

def info(**values):
    print('ТИП: ', type(values))
    print('Аргумент:', values)
    for key, value in values.items():
        print(key, value)

info(name='Denis', course="Python")

# Так же мы можем комбинировать параметры. ГЛАВНОЕ ** нужно использовать после *
# (именованные параметры и позиционные параметры)

def info(value, *types, name='Den', **values):
    print('ТИП: ', type(values))
    print('Аргумент:', values)
    for key, value in values.items():
        print(key, value)
    print(types)

info(1, 2, 3, 4, 5, name='Denis', course="Python")

# Находим сумму числе и возводить в степень

def my_sum(n, *args, txt='Сумма чисел'): # Функция моя сумма(степень, какое то количество параметров, текст
    s = 0 # Переменная, которая изначально хранит число 0
    for i in range(len(args)): # Функция И в диапазоне(длина не известна(наша функция)
        s += args[i] ** n # Берем нашу начально значение (перебираем список) И возводим в степень Н
        # Прибавляем к нашей переменной С
    print(txt + ':', s)

my_sum(1, 1, 2, 3, 4, 5)
my_sum(2, 1, 2, 3, 4, 5, txt='Сумма квадратов')







