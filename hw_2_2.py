# -*- coding: utf8 -*-

def sum_natural_numbers(a, b):
    sum_natural_num = 0
    for i in range(a, b+1):
        sum_natural_num += i
    if a == b:
        return a

    return sum_natural_num

cont = 1
stop = 2
while cont is not 2:
    print('Укажите начало и конец промежутка, который состоит'
          '\nтолько из натуральных чисел (начало промежутка должно быть больше,'
          'чем конец промежутка. Пример промежутка: [1, 2].)')
    print('=========================')
    a = input('Введите начало вашего промежутка: ')
    b = input('Введите конец вашего промежутка: ')
    print('=========================')

    if a.isdigit() and b.isdigit():

        if int(a) > 1 and int(b) > 1:

            if int(a) < int(b):
                print('Сумма всех натуральных чисел на промежутке [{0}, {1}] '
                      'равна: {2}'.format(a, b, sum_natural_numbers(int(a), int(b))))
            elif int(a) == int(b):
                print('Вы задали промежуток, которые состоит из одного натурального числа {0},'
                      'поэтому сумма всех чисел равна: {1}'.format(a, sum_natural_numbers(a, b)))
            else:
                print('Вы неверно указали промежуток( у вас начало промежутка больше, '
                      'чем конец промежутка ).')

        else:
            if int(a) < 1 and int(b) > 1:
                print('У вас начало промежутка меньше 1.')
            elif int(a) > 1 and int(b) < 1:
                print('У вас конец промежутка меньше 1.')
            elif int(a) < 1 and int(b) < 1:
                print('У вас начало и конец промежутка меньше 1.')
            else:
                print(sum_natural_numbers(int(a), int(b)))

    else:
        if not a.isdigit() and b.isdigit():
            print('Вы указали в начале промежутка ненатуральное число.')
        elif not b.isdigit() and a.isdigit():
            print('Вы указали в конце промежутка ненатуральное число.')
        else:
            print('В начале и конце промежутка вы указали ненатуральные числа.')

    print('Продолжить: 1')
    print('Остановиться: 2')
    s = input('Ваш выбор: ')

    if s == '1':
        continue
    elif s == '2':
        break
    else:
        print('Круг повторяется, пока вы в конце не выберите "2".')
'''        while s != '1' or s != '2':

            if s == '1':
                continue
            elif s == '2':
                break
            else: '''


