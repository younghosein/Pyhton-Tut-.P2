class car:
    def __init__(self,name , price):
        self.name = name
        self.price = price
    def show(self):
        print(f'i have a {self.name}')
    def __str__(self): #dunder methods
        return f'{self.name} - {self.price}'
    def __add__(self, other):
        return self.price + other.price
    def __len__(self):
        return len(self.name)

a = car('pegeut', 300)
b = car('bmw', 1100)

print(a)
print(a + b)
print(len(a))
print(len(b))