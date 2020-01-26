# -*- coding: utf8 -*-

a = int(input('Введите целое число: '))
int_num = a
float_num = float(a)
bool_num = bool(a)
str_num = str(a)
print('целое число: {0}'
      '\n вещественное число: {1}'
      '\n логическое значение: {2}'
      '\n строка: {3}'.format(int_num, float_num, bool_num, str_num))

b = int(input('Введите второе число: '))

sum_int_int = a + b
sum_int_float = a + float(b)
sum_int_bool = a + bool(b)
multi_int_int = a*b
multi_int_float = a*float(b)
multi_int_bool = a*bool(b)
multi_int_str = a*str(b)
sum_float_float = float(a) + float(b)
sum_float_bool = float(a) + bool(b)
multi_float_float = float(a) * float(b)
multi_float_bool = float(a) + bool(b)
sum_bool_bool = bool(a) + bool(b)
multi_bool_bool = bool(a) * bool(b)
multi_bool_str = bool(a) * str(b)

print(sum_int_int, ' = {0} + {1}'.format(a, b),
'\n', sum_int_float, ' = {0} + float({1})'.format(a, b),
'\n', sum_int_bool, ' = {0} + bool({1})'.format(a, b),
'\n', multi_int_int, ' = {0} * {1}'.format(a, b),
'\n', multi_int_float, ' = {0} * float({1})'.format(a, b),
'\n', multi_int_bool, ' = {0} * bool({1})'.format(a, b),
'\n', multi_int_str, ' = {0} * str({1})'.format(a, b),
'\n', sum_float_float, ' = float({0}) + float({1})'.format(a, b),
'\n', sum_float_bool, ' = float({0}) + bool({1})'.format(a, b),
'\n', multi_float_float, ' = float({0}) * float({1})'.format(a, b),
'\n', multi_float_bool, ' = float({0}) + bool({1})'.format(a, b),
'\n', sum_bool_bool, ' = bool({0}) + bool({1})'.format(a, b),
'\n', multi_bool_bool, ' = bool({0}) * bool({1})'.format(a, b),
'\n', multi_bool_str, ' = bool({0}) * str({1})'.format(a, b))
