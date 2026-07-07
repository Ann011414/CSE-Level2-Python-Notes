#变量和常量——把常亮赋值给变量
a=10
name="张三"
pi=3.14
print(a)
print("a")

Name="李四"
print(name,Name)

#数据类型——数值型 字符串型 布尔型
print(123)
print(0b1011) #这是二进制 11
print(0o123) #八进制 83
print(0x123) #十六进制 291
#输出的时候会变成十进制

#浮点型
f1=1.23 #将浮点数1.23赋值给变量f1
f2=1.01e4
print(f1,f2)

#复数
print(11.3+4j)
num=5+2j
print(num)

#获取复数的实部和虚部
print(num.real)
print(num.imag)

#字符串
print('hello world')
s="hello kitty"
print(s)

s2="""hello everyone ,
这里可以换行"""
print(s2)

#bool布尔类型
print(True)
print(False)

#type()  函数
a=123.393938
b=2+9j
print(type(a)) #注意此处想要输出，需要把type这个函数放在print里面
print(type(b))

#数据类型的转换
age="14"
age_new=int(age)
print("the type of age_new is",type(age_new))

a=2.3
b=int(a) #直接把小数部分给砍掉
print(b)



#运算符
x=10
y=4
z=3
print(x*y)
print(x/y) #除法运算 得到一个小数
print(type(x/y))
print(x//y)
print(type(x//y))
print(x%y)
print(x%z)
print(x**z)


#字符串的链接
s1="how"
s2=" are you"
print(s1+s2) #注意加号两边都要是字符串才行！！否则报错
print(s1*4)

#增强赋值操作符
a=3
b=5
a,b=b,a #将变量a和变量b中的值调换
print(a,b)
print("the value of a is"+str(a))


x=y=123
s1=s2="helloworld"
print(x,y)
print(s1,s2)

i=10
i+=1  #等价于i=i+1
print(i)


# 关系运算符——进行判断的操作，计算之后的结果都是bool类型
#注意等号和赋值号之间的区别 == 和 =
a=5
print(a==5) #进行判断，a是否等于5
print(a!=5)
print(a>=5) #输出TRUE


#逻辑运算符 not and or
"""
and 有假则假
or 有真则真
"""
a=5
b=6
print(a>5 and b==6) #有假则假，任意一边是false 结果就是false
print(a>5 or b==6)


#input()函数 用来接收键盘上输入的内容，接收的内容默认是字符串!!!!!
age =  input("请您输入年龄:")
print("年龄为"+age)
print(type(age))
#将接收到的年龄进行计算的话，需要先变换变量类型
age_new = int(age) + 10
print("加10之后的年龄是",age_new)


















