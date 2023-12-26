"""
created by: yashar zavary rezaie


simple num: usual int and float numbers
complex num: it is sin or other functional numbers
"""
import math

class Post:
    def __init__(self, infixForm):
        self.__infix = infixForm
        self.__postfix = Post.convertPostFix(infixForm)
        self.__result = Post.calcPosResult(self.__postfix)

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
    @staticmethod
    def convertPostFix(infixform):
        # TODO: if it is 2, we have other situations here
        """
        heart of the class! converting function
        :param infixform: infix form that user want to convert it
        :return: post fix form
        """
        # our valid variables
        commands = {')': 0, '+': 1, '-': 1,
                    '/': 2, '*': 2, '^': 3,
                    '(': 4}
        complexNums = ['sin', 'cos', 'tan', 'log']

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
                        while opList:
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

        ops = ['+', '-', '*', '/', '^']
        complexSolvers = {'sin': math.sin, 'cos': math.cos,
                          'tan': math.tan, 'log': math.log}

        results = []

        tempStr = postForm.split()

        for com in tempStr:
            if com[0:3] in complexSolvers.keys():
                results.append(complexSolvers[com[0:3]](int(Post.calcPosResult(com[4:len(com)-1]))))
            elif com in ops:
                results.append(eval(f'{results.pop(-2)} {com} {results.pop()}'))
            else:
                results.append(com)
        return results[0]

    def __str__(self):
        return f"post form: {self.__postfix}\nresult: {self.__result}"

    def __repr__(self):
        return self.__postfix
    def __del__(self):
        pass
