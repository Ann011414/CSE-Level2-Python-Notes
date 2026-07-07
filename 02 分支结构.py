"""
程序控制的三种结构：顺序结构 分支结构 循环结构 （背住）
顺序：就是说这个程序依次执行
分支（下面的名词和对应的方法都要记住）
 1）单分支结构
 2）二分支结构
 3）多分支结构
"""


#单分支结构
score = float( input("请输入你的成绩:"))
if score>=60: #注意缩进（如果没有缩进，按一下tab键）
    print("恭喜你，成绩及格！！！")
    print("成绩大于等于60分！！")

#二分支结构
score = float( input("请输入你的成绩:"))
if score>=60:#注意缩进（如果没有缩进，按一下tab键）
    print("恭喜你，成绩及格！！！")
    print("成绩大于等于60分！！")
else :
    print("不及格，准别补考吧！！！")

balance = 5000 #余额
money = int(input("请输入取款金额："))
if money <= balance and money % 100 == 0:
    print("正在准备中，请稍后。。。")
else:
    print("余额不足或者没有输入100的整数倍，挣钱去吧。。。")


#多分支结构
score = float(input("请输入你的成绩："))

if score >= 80 :
    print("成绩优秀")
elif score >=60 and score < 80 :
    #注意，此处的score < 80 这个条件不需要，因为能进入第二个条件，就一定是不符合第一个条件的
    print("普通及格")
else :
    print("不及格")

#嵌套的判断
if score >=60 :
    if score < 80:
        print("及格")
    else :
        print("great")
else :
    print("不及格！！！")


