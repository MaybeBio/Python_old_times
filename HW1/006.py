'''
判断 100 以内（所有数都在 1-100 之间且包含 100）所有的勾股数，并输出
其组数。所谓的勾股数就是指 3，4，5 或者 5，12，13 这样的一组数，前两个数
的平方和等于第三个数的平方。
'''
sum=0
for x in range(1,100):
    for y in range(x+1,100):
         z=int((x**2+y**2)**0.5)
         if x**2+y**2==z**2 and x+y>z and x+z>y and y+z>x and z<=100:
             print(x,y,z) 
             sum+=1
print(sum)


