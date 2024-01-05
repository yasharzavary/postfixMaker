# control panel


from postClass import Post
#
temp = Post('( ( 4 + 8 ) / ( 6 - 2 ) )')
# temp = Post('( x + x )')
print(temp.info())
print(temp.calcPosResult(temp))
# print('( x ^ 2 + cos(x) )'.replace('x', '5'))
# temp.drawLine()


