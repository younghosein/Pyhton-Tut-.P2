#class moshtari
class moshtari:
    #fields>shenase,tedadenanbarbari,tedadenanlavash
    def __init__(self, name,tedad_barbari, tedad_lavash):
        self.name = name
        self.tedad_lavash = tedad_lavash
        self.tedad_barbari = tedad_barbari

#Class nan
class nan:
    #fields>no'e(barbariORlavash)
    def __init__(self,type):
        self.type=type

#class saf halghavi
class CircularQueue():

    #tabe sazande,field>hade saf
    def __init__(self, size):
        self.size = size
        #sakhte safe halghavi khali
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    #tabe darj
    def enqueue(self, data):
        #if(por bod)
        if ((self.rear + 1) % self.size == self.front):
            print(" Queue is Full\n")

        #if(khali bod)
        elif (self.front == -1):
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            #taghire rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    #tabe hazf
    def dequeue(self):
        #if(khali bod)
        if (self.front == -1):
            print("Queue is Empty\n")

        #if(tak onsori bod)
        elif (self.front == self.rear):
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    #tabe namaieshe saf
    def display(self):

        #if(khali bod)
        if (self.front == -1):
            print("Queue is Empty")

        elif (self.rear >= self.front):
            print("Elements in the circular queue are:",
                  end=" ")
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")
            print()

        if ((self.rear + 1) % self.size == self.front):
            print("Queue is Full")

#class stack
class stck:
    #tabe sazande,field>hade saf
    def __init__(self, size):
        self.size = size
        #sakhte safe halghavi khali
        self.stack = [None for i in range(size)]
        self.top = -1

    def display(self):
        if self.top == -1:
            print("Stack is empty!")
            return
        for i in range(0,self.top+1):
            print(self.stack[i],end=" ")

    def push(self,d):
        if self.top==self.size-1:
            print("Stack is full!")
            return
        self.top=self.top+1
        self.stack[self.top]=d

    def pop(self):
        if self.top == -1:
            print("Stack is empty!")
            return
        self.top=self.top-1

#Driver Code
def init():
    cq_moshtariha = CircularQueue(10)
    st_lavash = stck(15)
    st_barbari = stck(15)
init()


