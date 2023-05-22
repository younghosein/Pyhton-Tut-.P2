with open('test.txt') as F:
    pass
    print(F.read())
    print(F.readlines())
    print(F.readline())
    print(F.readline())
    print(F.seek(34))
    print(F.read(24))
    print(F.tell())
print(F.closed)

with open('test2.txt', 'w') as F2:
    F2.write('HAAAAAAAA')

with open('test2.txt', 'a') as F2:
    F2.write('Uweeeeeee')