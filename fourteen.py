class car: #blueprint (halate koli)
    ...

a = car() #obj (instanse)
b = car()

a.name = 'pride' #attribiute (property)
b.name = 'benz'

a.price = 100 #dot notation
b.price = 900

print(a.price)
print(b.name)

print(f'{a.name} cost\'s {a.price}$')
print(f'{b.name} cost\'s {b.price}$')

class car2:
    def show(self):
        print('HAAAAAAAA :)')
        print(self)

c1 = car2()
c1.show()
print(c1)

c2 = car2()
c2.show()


class car3:
    def __init__(self,n , p): #Constractor (built-in)
        print("Class Initialized")
        self.name = n
        self.price = p
    def show(self):
        print(f'{self.name} cost\'s {self.price}$')

x = car3('206',300)
w = car3('bmw',1100)

x.show()
w.show()

print(f'{x.name} cost\'s {x.price}$')
print(f'{w.name} cost\'s {w.price}$')




