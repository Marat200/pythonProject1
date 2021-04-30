n = int(input('Введите количество элементов: '))
i = 0
range_number = 1
sum = 0
while i < n:
    sum += range_number
    range_number /= -2
    i += 1

print(f'Сумма {sum}')