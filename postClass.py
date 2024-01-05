"""
created by: yashar zavary rezaie


simple num: usual int and float numbers
complex num: it is sin or other functional numbers
"""
import math
from string import ascii_letters

class Ex(Exception):
    def __init__(self, message):
        super().__init__(message)
        self.__mes = message
    def __str__(self):
        return f'error: {self.__mes}'


class Post:
    def __init__(self, infixForm):
        self.__infix = infixForm
        self.__postfix = Post.convertPostFix(infixForm)
        self.__result = Post.calcPosResult(self.__postfix)

    def info(self):
        """
        it will get us some info about the formula,
        properties:
            1.number of numbers(nn)
            2.number of odd numbers(non)
            3.number of even numbers(nen)
            4.result
            5.post form
            6.infix form
            7.number of complex numbers(ncn)
        :param get:
        :return:
        """
        nn = 0
        non = 0
        nen = 0
        ncn = 0
        ops = ['+', '-', '*', '/', '^']
        for item in self.__postfix.split():
            if item not in ops:
                try:
                    if int(item) % 2 == 0:
                        nen += 1
                    else:
                        non += 1
                    nn += 1
                except:
                    ncn += 1
        return f"nn: {nn}\tnen: {nen}\tnon: {non}\tncn: {ncn}\ninfixForm: {self.__infix}\tpostForm: {self.__postfix}\nresult: {self.__result}"


    @property
    def postForm(self):
        """
        getting post form of the this object
        :return: post form in string type
        """
        return self.__postfix
    @property
    def result(self):
        return self.__result

    def drawLine(self, start=0, stop=0):
        import numpy as np
        import matplotlib.pyplot as plt
        def getSol(x):
            return Post.calcPosResult(self.postForm.replace('x', f'{x}'))

        if 'sqrt' in self.postForm or 'log' in self.postForm:
            if start == 0 and stop == 0: x = np.linspace(0, 100, 100)
            elif start == stop or start < stop: raise Ex('start and stop is false')
            elif start < 0: raise TypeError('you can\'t use negative number in this equation')
            else: x = np.linspace(start, stop, 100)
        else:
            if start == 0 and stop == 0: x = np.linspace(-50, 50, 100)
            elif start == stop or start < stop: raise Ex('start and stop is false')
            else: x = np.linspace(start, stop, 100)
        y = []
        for num in x:
            y.append(getSol(num))
        plt.plot(x, y)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('diagram of equation you give')
        plt.grid()
        plt.show()


    @staticmethod
    def convertPostFix(infixform):
        # TODO: if it is 2, we have other situations here
        # TODO: false math formula error must added
        """
        heart of the class! converting function
        :param infixform: infix form that user want to convert it
        :return: post fix form
        """
        # our valid variables
        commands = {')': 0, '+': 1, '-': 1,
                    '/': 2, '*': 2, '^': 3,
                    '(': 4}
        complexNums = ['sin', 'cos', 'tan', 'log', 'sqrt']

        # split the numbers and operators
        infixSplitForm = infixform.split()

        # empty lists for our operators and numbers
        opList = []
        nums = []
        # main part
        for com in infixSplitForm:
            # check the complex nums
            if com[0:3] in complexNums:
                # adding complex num part
                nums.append(com[0:3] + Post(com[3:]).postForm)
            elif com in commands.keys():
                # if it is empty or higer value operator, adding to the op list
                if not opList or commands[com] >= commands[opList[-1]] or opList[-1] == '(':
                    opList.append(com)
                else:
                    # if it is paranteses, it will until reach the nearst (
                    if com==')':
                        while opList[-1] != '(':
                            nums.append(f'{nums.pop(-2)} {nums.pop()} {opList.pop()}')
                        opList.pop()
                    # otherwise it will add until op list get empty
                    else:
                        while opList and opList[-1] != '(':
                            nums.append(f'{nums.pop(-2)} {nums.pop()} {opList.pop()}')
                        opList.append(com)
            else:
                # if it is simple num, add to the num list
                nums.append(com)

        # unitl finishing the op list, it will add to the num list
        while opList:
                nums.append(f'{nums.pop(-2)} {nums.pop()} {opList.pop()}')
        # return the result
        return nums[0]

    @staticmethod
    def calcPosResult(postForm):
        # TODO: post checker
        # TODO: error handling(1: it is variable type or not)
        if isinstance(postForm, Post): postForm = postForm.postForm
        if 'x' in postForm:return 'variable type equation'
        ops = ['+', '-', '*', '/', '^']
        complexSolvers = {'sin': math.sin, 'cos': math.cos,
                          'tan': math.tan, 'log': math.log,
                          'sqrt': math.sqrt}

        results = []

        tempStr = postForm.split()
        for com in tempStr:
            if com[0:3] in list(complexSolvers.keys()):results.append(complexSolvers[com[0:3]](float(Post.calcPosResult(com[4:len(com)-1]))))
            elif com[0:4] in list(complexSolvers.keys()):results.append(complexSolvers[com[0:4]](float(Post.calcPosResult(com[5:len(com)-1]))))
            elif com in ops:
                if com == '^':results.append(eval(f'{results.pop(-2)} ** {results.pop()}'))
                else: results.append(eval(f'{results.pop(-2)} {com} {results.pop()}'))
            else:
                results.append(com)
        return results[0]

    def __str__(self):
        return f"post form: {self.__postfix}\nresult: {self.__result}"

    def __repr__(self):
        return self.__postfix
    def __del__(self):
        pass
