"""
循环结构
遍历循环：for
无限循环：while

"""


# while 循环
i = 0
while i<10:
    print("helloworld")
    i+=1

i=1
sum=0
while i <=100:
    sum=sum+i
    i+=1
print(sum)

#循环控制 continue 用来结束当前本次循环，continue后面的内容不会执行，然后继续执行下一次循环
#此代码的需求是，输出1-100之间所有的偶数
"""
i=0
while i<= 100:
    i=i+1
    if i % 2 == 0:
        print(i)
"""

i=0
while i<= 100:
    i=i+1
    if i % 2 == 1:
        continue #这个continue会跳过此次循环，就是说后面的print不会被执行
    print(i)


#break 终止所在循环
#输出1-100 的前三个偶数
count = 0
i=0
while i <= 100:
    i=i+1
    if  i%2 == 0:
        print(i)
        count +=1
    if count == 3:
        break




### for 循环
s="how are you doing"
for i in s:
    print(i)  #依次输出每个字母











