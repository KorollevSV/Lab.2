#!/usr/bin/env python3
import random 

from librip.gens import field

goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Стелаж', 'price': 7000, 'color': 'white'},
    {'title': 'Вешалка для одежды', 'price': 800, 'color': 'white'}
]

# Реализация задания 1

#Генератор field последовательно выдает значения ключей словарей массива
def feild (items, *args):
    assert len (args) >0, 'No keys. At least one keys needed'
    if len(args)==1:
        for item in items:
            if args[0] in item:
                yield item[args[0]]

    else:
        for item in items:
            d = {arg: item[arg] for arg in args if arg in item}
            if len(d) > 0:
                yield d

#Генератор gen_random последовательно выдает заданное количество случайных чисел в заданном диапазоне
def gen_random(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)


print(list(gen_random(2,7, 5)))
print(list(feild(goods, 'title')))
print(list(feild(goods, 'title', 'price')))
print(list(feild(goods, 'title', 'color')))


