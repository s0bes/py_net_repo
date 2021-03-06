# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

filename = 'CAM_table.txt'
f_str = '{:10}{:15}{:>10}'
vlan_dict = []

vlan_num = input('Введите номер vlan:\n')

with open(filename, 'r') as f:
    for line in f:
        if line.find('DYNAMIC') != -1:
            vlan, mac, typ, intf = line.split()
            if vlan == vlan_num:
                print(f_str.format(vlan, mac, intf))
