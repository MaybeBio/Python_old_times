#定义函数 monthdays(year, month)用来求参数月份和年份的天数，通过不同参数调用该
#函数验证结果。
def monthdays(year, month:int)->int:
    '''
    用来求参数月份和年份的天数
    '''
    if month in (1, 3, 5, 7, 8, 10, 12):
        print(31)
    elif month in (4, 6, 9, 11):
        print(30)
    elif year % 400 == 0 or year % 4 == 0 and year % 100 != 0:  #闰年
        print(29)
    else:
        print(28)
monthdays(2000,2)
monthdays(2000,1)
monthdays(2001,2)
