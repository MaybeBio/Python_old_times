#1、定义函数 isprime 判断某个整数是否为素数，要求当参数为素数时返回 True，否则返回False。
#调用该函数验证孪生素数问题——输入一个整数 n，总能在 n 的后面找到两个素数只差 2
#，如输入 100，则输出 101 和 103。
def isprime(n:int)->bool:
    '''
    判断某个整数是否为素数，要求当参数为素数时返回 True,否则返回False
    '''
    if n==2:
        return True
    elif n%2==0:
        return False
    k=int(n**0.5)
    for i in range(3,k+1,2):
        if n%i==0:
            return False
    return True
print(isprime(37))
print(isprime(240))
n=int(input('输入一个整数 n:'))
while(1):  #永真循环，由break退出,若用for只能指定范围内找
    if(isprime(n) and isprime(n+2)):
        print(n,n+2)
        break
    n+=1


