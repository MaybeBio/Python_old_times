age=int(input('请输入你的年龄：'))
if(age<18):
    print("不准进")
elif(age<30):
    print('还可以')
    if(age>25):
        print("有点难说，你的年龄已经是%d了！"%age)
else:
    print("太老了，也不准进")