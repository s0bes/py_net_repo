# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

f_str = "Prefix {pref}\nAD/Metric {metr}\nNext-Hop {hop}\nLast update {upd}\nOutbound Interface {int}\n"


with open('ospf.txt', 'r') as f:
    for line in f:
        line = line.replace('[','').replace(']','').replace(',','').split()
        print(f_str.format(pref = line[1], metr = line[2].replace('[',''), hop = line[4], upd = line[5], int = line[6]))
