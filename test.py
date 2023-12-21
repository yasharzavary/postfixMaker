

class p:


    def __init__(self):
        self.hello = self.sayHello()

    def sayHello(self):
        return 'yes'


    def come(self):
        print(self.sayHello())




x = p()
x.come()
