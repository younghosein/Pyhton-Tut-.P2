class car:
    wheel=4
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f'i have a {self.name}')

class motor(car):
    wheel = 2
    def show(self):
        super().show()
        print(f'i ride {self.name}')
    def __init__(self, name, helmet):
        super().__init__(name)
        self.helmet = helmet
    
#m = motor('honda')
#m.show()
m = motor('honda', 'no')
m.show()
#help(m)

class object:
    pass