import random

n = random.randint(0, 10)
b = random.randint(0, 10)


while True:
    a = int(input('Введіть відповідь на приклад {0} = a + {1}:\n'.format(b, n)))
    if n + a == b:
        print('Молодец')
        break
    else:
        print('Спробуй щє')
