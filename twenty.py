class person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def fullName(self):
        return f'{self.fname} {self.lname}'
    
    @property
    def email(self):
        return f'{self.fname}_{self.lname}@gmail.com'

a = person('andrew', 'tate')
a.fname = 'topGi'
print(a.fname)
print(a.lname)
print(a.email)
print(a.fullName())