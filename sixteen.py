import datetime
res = datetime.datetime.now().year
print(res)

class person:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

    def show(self): #Instance
        print(f'{self.name} is {self. height} and has {self.age} years old')

    @classmethod
    def fromBirth(cls, name, height, age): #Class
        return cls(name, height, res-age)

    @staticmethod
    def isAddult(age): #Static
        if age > 18:
            print('yes')
        else:
            print('No')

p1 = person.fromBirth('hosein', 188, 2002)
p1.show()

person.isAddult(21)