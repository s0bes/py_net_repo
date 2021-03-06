# -*- coding: utf-8 -*-
"""
Задание 5.3a

Дополнить скрипт из задания 5.3 таким образом, чтобы, в зависимости
от выбранного режима, задавались разные вопросы в запросе о номере
VLANа или списка VLANов:
* для access: 'Введите номер VLAN:'
* для trunk: 'Введите разрешенные VLANы:'

Ограничение: Все задания надо выполнять используя только пройденные темы.
То есть эту задачу можно решить без использования условия if и циклов for/while.
"""


access_template = [
    "interface {interface}",
    "switchport mode access",
    "switchport access vlan {vlans}",
    "switchport nonegotiate",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_template = [
    "interface {interface}",
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan {vlans}",
]

quest_template = {
    'access' : 'Введите номер VLAN:\n',
    'trunk' : 'Введите разрешенные VLANы:\n'
}

mode = {
    'access' : access_template,
    'trunk': trunk_template
}

reg = input('Введите режим работы интерфейса (access/trunk):\n')
int_num = input('Введите тип и номер интерфейса:\n')
vlan_num = input(quest_template.get(reg))

print('\n'.join(mode.get(reg)).format(interface = int_num,vlans = vlan_num))
