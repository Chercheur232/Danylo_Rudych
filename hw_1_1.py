# -*- coding: utf8 -*-


name = input('Ваше имя: ')
print('Добрый день, {0}. '.format(name))

birth_day = input('Введите день вашего рождения: ')
birth_month = input('Введите месяц вашего рождения: ')
birth_year = input('Введите год вашего рождения: ')

already_lived_year = 2020 - int(birth_year)
already_lived_month = already_lived_year * 12

#condition: already've lived to 10.01.2020 without leap-year, 30 days in month
leap_year = already_lived_year//4
already_lived_year_with_condition = 2020 - int(birth_year) - leap_year 
already_lived_month_with_condition = already_lived_year_with_condition * 12 - 1
already_lived_day_with_condition = already_lived_month_with_condition * 30  - 20
print('Кол-во прожитых лет: ', already_lived_year,
      '\n==='
      '\nКол-во прожитых месяцев: ', already_lived_month,
      '\n==='
      '\nКол-во прожитых дней, месяцев, лет '
      'до даты начала курса 10.01.2020 - без учёта '
      '\nвисокосных лет и среднее количество дней в месяце считать 30: {0} дней, {1} лет, {2} месяцев'.format(
          already_lived_day_with_condition, already_lived_year_with_condition, already_lived_month_with_condition
      ) )