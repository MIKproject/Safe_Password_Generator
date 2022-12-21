from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
chars = ''

quantity_psw = input('Введите количество паролей для генерации: ')
length_psw = input('Введите длину пароля: ')

if input('Включать ли цифры? (yes/no): ') in 'yes':
    chars += digits
if input('Включать ли прописные буквы? (yes/no): ') in 'yes':
    chars += uppercase_letters
if input('Включать ли строчные буквы? (yes/no): ') in 'yes':
    chars += lowercase_letters
if input('Включать ли символы? (yes/no): ') in 'yes':
    chars += punctuation
if input('Исключать ли неоднозначные символы il1Lo0O? (yes/no): ') in 'yes':
    for i in 'il1Lo0O':
        chars = chars.replace(i, '')


def generate_password(char, length):
    return sample(char, int(length))


for _ in range(int(quantity_psw)):
    print(*generate_password(chars, length_psw), sep='')
    
