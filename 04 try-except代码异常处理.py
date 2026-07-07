## 代码中的异常处理
#try-except 如果try中的代码出现了异常，就会执行except里面的内容

score = float(input("please enter your score:"))
print(score)

#此时如果输入的不是一个数值，就会出现代码异常

try:
    score = float(input("please enter your score:"))
    print(score)
except:
    print("程序出错了，请稍后。。。")

#一旦出错，就会执行except里面的内容
try:
    a=5
    b=0
    print(a/b)
except ZeroDivisionError:
    print("这里不能除以0")
except:
    print("出错了。。。")
    
