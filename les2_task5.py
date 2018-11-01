'''
Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32
и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар «код-символ» в каждой строке.
'''

START = 32
FINISH = 127
for i in range(START, FINISH, 10):
    txt = ''
    for n in range(10):
        if i + n <= FINISH:
            txt += f'{i + n}-{chr(i + n)}\t'
    print(txt)



