def fy(x):
    return x*3


lis = list(range(10))

print(lis)

lis2 = list(map(fy, lis))
print(lis2)

a = []
# объявляем пустой список
n = int(input("Введи количество символовб а потом символы: \n"))
# считываем количество элемент в списке
for i in range(n):
    a.append(int(input()))
print(a)

A = [int(input()) for i in range(int(input()))]

print(A)
