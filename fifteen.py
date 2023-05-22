class car:
    Obj_nums = 0
    wheel = 4
    def __init__(self,n , p):
        self.name = n
        self.price = p
        car.Obj_nums += 1
    def show_W(self):
        print(f'{self.name} cost\'s {self.price}$ & has {self.wheel} wheel')

c1 = car('206',300)
c2 = car('bmw',1100)
print(car.Obj_nums)

print(c1.__dict__)
print(c2.__dict__)
print(car.__dict__)

c1.wheel = 5
c1.show_W()
c2.show_W()

print(c1.__dict__)
print(c2.__dict__)
print(car.__dict__)