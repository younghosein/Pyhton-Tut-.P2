class person:
    name = 'hosein' #public
    _age = 21 #protected
    __height = 188 #private
    def __show(self):
        print('this is private')

class male(person):
    def show(self):
        print(self._age)
        #print(self.__height)

m = male()
m.show()
print(person._age)

p = person()
#print(person.__height) |X|
print(person._person__height)

p._person__show()