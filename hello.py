print("Hello Master")
name = input('Print yourname here:  \n')
name2 = list(map((lambda x: x*2), name))
print(name2)
name3 = ''.join(name2)
print('Letss fun  {}'.format(name3))



