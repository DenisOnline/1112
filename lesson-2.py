import random
from random import randint


def name_function():
    pass


def hello_world():
    a = "Hello World"
    return a


def summ(x, y=2):
    return x + y


def math(x, y, z):
    return x * 3 + (y / 2 - z + 5) * 4


def appender(count, list=[]):
    list.append(count)
    return list


def coin_simulator():
    coin = randint(0, 1)
    if coin == 0:
        return 'Орел'
    else:
        return 'Решка'


def oil():
    c = (random.randint(0, 1))
    x = int(input('Орел или Решка'))
    if c == x:
        return 'Win'
    else:
        return 'Проиграл'


while True:
    print(oil())
# print(math(x=3, y=6, z=2))
# print(math(3, 6, z=2))
# print(summ(2))
# print(summ("Hi ","World"))
# print(summ("Hi ",4))#error
# print(summ(int(input()), int(input())))