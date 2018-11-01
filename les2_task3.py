'''
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.
'''


num = int(input('Введите число: '))
n = 1
num_ch = 0
num_nech = 0
num_ch_num = 0
num_nech_num = 0

while 10 ** (n - 1) < num:
    cifra = num % (10 ** n) // (10 ** (n - 1))
    if cifra % 2 == 0:
        num_ch += cifra * 10 ** (num_ch_num)
        num_ch_num += 1
    else:
        num_nech += cifra * 10 ** (num_nech_num)
        num_nech_num += 1
    n += 1

print(f'Четные цифры из числа {num}:   {num_ch}')
print(f'Нечетные цифры из числа {num}: {num_nech}')