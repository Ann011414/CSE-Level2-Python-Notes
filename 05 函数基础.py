# 函数
def fun():
    sum=0
    i=1
    while i<= 100:
        sum+=i
        i+=1
    print(sum)

#fun()#注意，对于函数一定要调用才能被执行


def add(a,b):
    print(a+b)

add(3,4)#注意传参的时候需要根据顺序传参

#返回值  return<返回值>
def add(a,b):
    return a+b

s=add(3,5)
print(s)



#可以返回多个返回值
def fun(a,b):
    return b,a

print(fun(3,4))
print(type(fun(3,4)))

n,m=fun(3,4)
print(n,m)

#参数的传递 不同场景如何使用参数和返回值  可选参数
"""
形参：函数声明时候的参数
实参
"""
def fun(a,b):
    print(a+b)#a  b  就是形参

fun(5,6)  #5 6 就是实参

def fun(a):
    a=5
    print(a)

m=10
fun(m) #值传递，对m的值没有改变
print(m)

#不同场景如何使用参数和返回值（有/无参数   有/无返回值）
def fun1():
    sum=0
    i=1
    while i<=100:
        sum+=i
        i+=1
    print(sum)

    
def fun2():
    sum=0
    i=1
    while i<=100:
        sum+=i
        i+=1
    return sum
print(fun2())


def fun3(s):
    if s>=60:
        print("及格")
    else:
        print("不及格")

def fun4(s):
    if s>=60:
        return True
    else:
        return False



#可选参数
#声明一个函数，可以计算两个数相加的和，默认第二个数是5，也可以传入参数改变
def fun(a,b=5):  #注意这个可选参数要写在普通参数后面
    print(a+b)

fun(10)
fun(2,3)


###函数的作用域
"""
局部变量：只在函数内部定义的变量，仅在函数内部有效，当函数退出时，变量不再存在
全局变量：函数之外定义的变量；全局变量在函数内部使用时，需要用 global<全局变量> 来声明
"""
n=2
def fun(a,b):
    n=a*b
    print(n)  #这个里面声明的局部变量n与外面的那一个没有任何关系，不会修改全局变量n的值
    
fun(5,6)
print(n)


n=2
def fun(a,b):
    global n  #此时声明使用的是外面的n，可以直接改变全局变量
    n=a*b
    print(n)
    
fun(5,6)
print(n)


### print 函数输出不换行的方式
# print(<待输出的内容>,end="<增加的输出结尾>")
a=2026
print(a,end="")
print(a)











