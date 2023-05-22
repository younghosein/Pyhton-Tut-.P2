#print 'hello'
#print(1 / 0)
#print(2 + 2 - '3')
#f = open('text3.txt')
#print(str.upper(32))


try:
    f = open('test2.txt')
    print(str.upper(32))
except TypeError :
    print('baiad string bashe haji !!')
except FileNotFoundError :
    print('filet vojod ndare')
else:
    print('A F A R I N')
finally:
    print('I don\'t care')

try:
    print(str.upper(32))
except Exception :
    print('ERORRRRRRR')

x = 2
if x == 2:
    raise Exception('x nabas 2 bashe haji')
