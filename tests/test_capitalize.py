# coding=cp1251

from capitalize import capitalize

if capitalize('hello') != 'Hello':
  raise Exception('������� �������� �������!')

if capitalize('') != '':
  raise Exception('������� �������� �������!')

if capitalize('_') != '_':
  raise Exception('������� �������� �������!')

if capitalize('�') != '�':
  raise Exception('������� �������� �������!')
  
if capitalize(null) != null:
  raise Exception('������� �������� �������!')

if capitalize(5) != '5':
  raise Exception('������� �������� �������!')

  
print('��� ����� ��������!')