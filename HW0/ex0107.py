x=int(input("请输入一个三位数"))
a=x//100
b=x//10%10
c=x%10
y=c*100+b*10+a
input("倒序的结果是")
print(y)