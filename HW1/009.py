'''
9、设计递推算法，实现自然对数 ex=1+x/1!+x2/2!+…+xn/n!，精度为 10 的-6 次方。
求指数e的一个精确表示
'''
sum,tmp = 1, 1
for i in range(1, 20):
    tmp *= i
    sum += 1/tmp
print("e的近似值(精度为10**-6)为%.6f" % sum)
