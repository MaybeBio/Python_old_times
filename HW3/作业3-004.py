#4、定义函数 student_grade(name , age , gender = ‘男’, *score)，对学生的成绩进
#行判断。通过 score 获取任意多门的成绩，并求出其均分。如果均分>=90，返回“优”；如
#果>=80，返回“良”；如果>=70，返回“中”，如果>=60 返回“及格”，60 以下返回“不
#及格”；如果 score 无输入，则返回“无效”
#通过不同参数调用该函数，输出学生信息和等级。
from statistics import mean
def student_grade(name , age , gender = '男', *score):
    if(score==()):   #元组参数
        level="无效"
    elif(mean(score)>=90):
        level="优"
    elif(mean(score)>=80):
        level="良"
    elif(mean(score)>=70):
        level="中"
    elif(mean(score)>=60):
        level="及格"
    else:
        level="不及格"
    print(name , age , gender,level)
student_grade('tom',12,'男',98,97,96)
student_grade('tom',12,'男',88,87,86)
student_grade('tom',12,'男',78,77,76)
student_grade('tom',12,'男',68,67,66)
student_grade('tom',12,'男',58,57,56)
student_grade('tom',12,'男')