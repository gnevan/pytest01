# coding=cp1251

from capitalize import capitalize

if capitalize('hello') != 'Hello':
  raise Exception('Функция работает неверно!')

if capitalize('') != '':
  raise Exception('Функция работает неверно!')

if capitalize('_') != '_':
  raise Exception('Функция работает неверно!')

if capitalize('ё') != 'Ё':
  raise Exception('Функция работает неверно!')
  
if capitalize(null) != null:
  raise Exception('Функция работает неверно!')

if capitalize(5) != '5':
  raise Exception('Функция работает неверно!')

  
print('Все тесты пройдены!')