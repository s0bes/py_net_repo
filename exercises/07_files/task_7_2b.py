# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv
file_in = argv[1]
file_out = argv[2]

ignore = ["duplex", "alias", "configuration"]

with open(file_in, 'r') as f, open(file_out,'w') as out:
    for line in f:
        if not line.startswith('!'):
            for ign in ignore:
                if line.find(ign) != -1:
                    break
            else:
                out.write(line)
