from math import sin

def sub(x, y):
    return x - y


def mul(x, y):
    return x * y


def add(x, y):
    return x + y


def div(x, y):

    return x / y



def quad(x, y):
    return x ** y

def sin_num(x):
    return sin(x)


calculator = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': quad
}

calc_func = {
    'sin': sin_num
}