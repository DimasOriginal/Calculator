from math import sin, cos

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

def cos_num(x):
    return cos(x)


calculator = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': div,
    '**': quad
}

calc_func = {
    'sin': sin_num,
    'cos': cos_num
}