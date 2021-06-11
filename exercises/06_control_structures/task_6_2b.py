# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ok_flag = False
while(not ok_flag):
    ip = input('Введите IP адрес:\n')
    octs = ip.split('.')
    
    ok_flag = (len(octs) == 4)
    for o in octs:
        ok_flag = o.isdigit() and int(o) in range(256) and ok_flag

    if not ok_flag:
        print('Неправильный IP-адрес\n')
    else:
        octet = int(ip[0:ip.find('.')])
        if 0<octet<224:
            print('unicast')
        elif 223<octet<240:
            print('multicast')
        elif ip == '255.255.255.255':
            print('local broadcast')
        elif ip == '0.0.0.0':
            print('unassigned')
        else:
            print('unused')
