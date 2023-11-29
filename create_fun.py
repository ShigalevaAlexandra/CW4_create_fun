# Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
# которая в качестве аргумента принимает другую функцию (главное, не встроенную, built-in).
# В результате работы она выводит следующие данные: название анализируемой функции,
# наименование всех принимаемых ею параметров и их типы (позиционные, ключевые и т.п.).
# Попробуйте повторить результат девушки.

import inspect
import math

def start_work_programm():
    inspect_function(new_function)
    inspect_function(summa)
    inspect_function(math.sqrt)


def inspect_function(function):
    print(f'\nAнализируем функцию - {function.__name__}')

    params = inspect.signature(function).parameters.values()

    for arg in params:
        print(arg.name, arg.kind, sep=': ')

    print("_"*25)

def new_function(a = 10, /, d = 2, *args, **key):
    pass

def summa(a, b):
    return (a + b)

start_work_programm()