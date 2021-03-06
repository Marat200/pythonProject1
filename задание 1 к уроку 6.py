'''
x86_64 GNU/Linux
Python 3.8
'''
'''
Размер листа больше, чем неизменяемый кортеж, с одним набором данных
(912 байт у листа 848 байт у кортежа). Размер не зависит от разрядности чисел.
Зависит от размера массива.
Каждый элемент массива занимает 28 байт. 100 элементов по 28 байт занимают
2800 байт. Это значительно больше размера массива этих данных, т.к. Python
делает оптимизацию и создаёт ссылки на один и тот же объект.
'''

import random
import sys

r = [random.randint(0, 99) for _ in range(100)]
print(f'Массив: {r}')

min_index_1 = 0
min_index_2 = 1

for i in r:
    if r[min_index_1] > i:
        min_index_2 = min_index_1
        min_index_1 = r.index(i)
    elif r[min_index_2] > i:
        min_index_2 = r.index(i)

print(f'Два наименьших элемента: {r[min_index_1]} и {r[min_index_2]}')

print('Размер листа', sys.getsizeof(r))
print('Размер элемента листа', sys.getsizeof(r[0]))
print('Размер кортежа', sys.getsizeof(tuple(r)))
print('Размер элемента кортежа', sys.getsizeof(tuple(r)[0]))
sum = 0
for size in r:
    sum += sys.getsizeof(size)
print('Размер всех элементов в листе', sum)