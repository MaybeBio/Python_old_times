'''
7、输出 1-10000 以内所有的同构数。所谓同构数是指一个数 n，正好是其平方
数的尾数。如 6 的平方是 36，76 的平方是 5776，则 6 和 76 都是同构数。
'''
for i in range(10000):
   k = str(i * i)                            #平方数
   if(len(k) % 2 == 0):
        m = int(k[(len(k) // 2):len(k)])     #取后位数
        if(m == i):
            print(m,end=" ")
   else:
        m = int(k[((len(k) + 1) // 2) - 1:len(k)])
        if(m == i):
            print(m,end=" ")