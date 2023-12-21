from postClass import Post

class p:


    def __init__(self):
        self.hello = self.sayHello()

    def sayHello(self):
        return 'yes'


    def come(self):
        print(self.sayHello())



# x = [1,2,3,4,5,6]
# print(x.pop(-2))
# print(x.pop())
# print(x)


# x = Post('256 / 6 + 856 * 5 - 78 * sin(25)')
x = Post('2.56 * 75 / 78 ^ 2 - 65 * ( 48 + 2 ) / 4')
# x = Post('5 + ( 42 + 78 )')
print(x.postForm)
