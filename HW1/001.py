# 1、从键盘输入两个正整数 n 和 a，
# 求 a + aa + aaa + … a..a(此处一共 n 个)的值。
# 例如：输入 n 是 3，a 是 1，则 1 + 11 + 111 = 123
# 提示：使用递推算法，从前一项变化得到后一项。
# a,n=map(int,input('请输入两个正整数：').split())
def fn(a, n):
    sum = res = 0
    for i in range(1, n+1):
        sum = sum+a
        a = a*10
        res = res+sum
    return res
a,n=map(int,input('请输入两个正整数：').split())
print(fn(a,n))

