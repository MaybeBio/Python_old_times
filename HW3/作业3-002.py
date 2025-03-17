#2、编写一个求三角形面积的函数，参数为三边长，返回值为一个小数。从键盘输入三边的
#长度，调用该函数求三角形的面积并输出结果。
#提示：如果输入三边不合理，如何处理？如输入的长度是 1 1 3?

#先写一个判断3边合理的函数
def legal(a,b,c:float)->bool:
    '''
    如果输入三边不合理，如何处理？如输入的长度是 1 1 3?
    不合理输出false,否则是true
    '''
    if(a+b>c and b+c>a and a+c>b):
        return True
    else:
        return False
#再写一个计算三角形面积的函数，利用海伦公式
def area(a,b,c:float)->float:
    '''
    编写一个求三角形面积的函数，参数为三边长，返回值为一个小数。从键盘输入三边的长度，调用该函数求三角形的面积并输出结果
    '''
    if legal(a,b,c):
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print("三角形面积是%0.2f"%area)
    else:
        print("不合法")
area(3,4,5)
area(1,1,3)