import random
'''Задан список слов. Необходимо выбрать из него случайное слово. Из выбранного /
 случайного слова случайно выбрать букву и попросить пользователя ее угадать.'''

list_of_words = ['самовар', 'весна', 'лето']


print('Привет, давай поиграем')
print('Попробуй угадать случайную букву из набора слов {}'.format(list_of_words))
random_word = random.choice(list_of_words)
random_latter = random.choice(list(random_word))

x = str()
i = 0
while x != random_latter:
    x = input('Введи  букву: \n')
    i = i + 1
    if x == random_latter:
        print("Молодец")
        break
    if len(x) > 1:
        print('Сказано введи ОДНУ букву')
    if x == 'стоп':
        print('Слабак')
        break


print("Задан список слов: ['самовар', 'весна', 'лето'")
print("Выбрано случайное слово: {}".format(random_word))
print("Выбрано случайная буква: {}".format(random_latter))
