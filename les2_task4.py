'''
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''

n = int(input('Введите число: '))
summ = 0
for i in range(n):
    a = 1 / 2 ** i * (-1) ** i
    if a == 1:
        a = int(a)
    #print(a)
    summ += a
print(summ)
