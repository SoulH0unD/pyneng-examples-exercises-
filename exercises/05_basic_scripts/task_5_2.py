# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Вывод сети и маски должен быть упорядочен также, как в примере:
- столбцами
- ширина столбца 10 символов (в двоичном формате
  надо добавить два пробела между столбцами
  для разделения октетов между собой)

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'
Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
vvod = input("Введите IP (пример: 10.1.1.0/24):")

ip, mask = vvod.split('/')

octets = ip.split('.')
output_ip = """
Network:
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

output_mask = """
Mask:
/{4}
{0:<10}{1:<10}{2:<10}{3:<10}
{0:08b}  {1:08b}  {2:08b}  {3:08b}"""

print(output_ip.format(int(octets[0]),int(octets[1]),int(octets[2]),int(octets[3])))
ip_mask = "1" * int(mask) + "0" * (32 - int(mask))
octets_mask = []
octets_mask.append(int(ip_mask[0:8], 2))
octets_mask.append(int(ip_mask[8:16], 2))
octets_mask.append(int(ip_mask[16:24], 2))
octets_mask.append(int(ip_mask[24:32], 2))

print(output_mask.format(int(octets_mask[0]),int(octets_mask[1]),int(octets_mask[2]),int(octets_mask[3]),mask))