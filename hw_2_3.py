# -*- coding: utf8 -*-

def fibonacci(n):
    print('Ряд чисел Фибоначчи, начиная с 1 по {0}: '.format(n))
    if n in (1, 2):
        return 1
    fib1, fib2 = 1, 1
    print(fib1, end = ' ')
    print(fib2, end = ' ')
    for i in range(2, n):
        fib1, fib2 = fib2, fib1 + fib2
        print(fib2, end = ' ')

if __name__ == "__main__":
    n = input('Введите число, до которого хотите вывести ряд Фибоначчи: ')
    while not n.isdigit() or int(n) < 1:
        n = input('Введите натуральное число: ')
    if n.isdigit():
            print(fibonacci(int(n)))