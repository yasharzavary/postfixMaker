import math

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
# x = [1,2,3,4,5,6]
# for i in x:
#     if i == 3:
#         x.remove(1)
#         x.remove(2)
#     print(i)
import math
# x = Post('256 / 6 + 856 * 5 - 78 * sin(25)')
# x = Post('2.56 * 75 / 78 ^ 2 - 65 * ( 48 + 2 ) / 4')
# x = Post('x + x * x / sin(x) - x * x ^ 2x')
l = '5 + log(8) - 6 + 8'
x = Post(l)
print(x)
# print(eval(l))

# print(math.sin(56))


