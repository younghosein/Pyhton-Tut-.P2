name1 = 'Sud'
age1 = 22
print(name1 + ' is ' + str(age1) + ' years old')

name2 = 'Chvrs'
age2 = 23
print(f'{name2} is {age2} years old')

name3 = 'Doki'
age3 = 24
print('{} is {} years old'.format(name3, age3))

info = {'n':'KAKA', 'a':25}
info2 = {'n':'KIKI', 'a':26}
print('{0[n]} is {0[a]} years old & {1[n]} is {1[a]} years old'.format(info,info2))

a = 10
def show():
    global a
    print(a)
    a = 20
show()
print(a)