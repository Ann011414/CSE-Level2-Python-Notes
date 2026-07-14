"""
import <模块名> as <别名>

from <模块名> import <对象、函数。。。>
"""
# 辅助文件：test_model_13

import test_model_13
test_model_13.fun1()

import test_model_13 as t
t.fun1()

from test_model_13 import fun1,fun2 #此时下面就不用再使用fun1的前面加上test_model_13
fun2()

#-------------------------------------------------------------------------------

import random
print(random.random())

from random import * #这个代表把random里面所有的函数都引入
print(randint(1,10))

#---------------------------------------------------------------------
### 内置函数
"""
abs(x)	        x 的绝对值。如果 x 是复数，返回复数的模
divmod(a, b)	返回 a 和 b 的商及余数。如 divmod (10, 3) 结果是一个 (3, 1)
pow(x, y)	返回 x 的 y 次幂。如 pow (2, pow (2, 2)) 的结果是 16
round(n)	四舍五入方式计算 n。如 round (10.6) 的结果是 11
"""

a=-1
print(abs(a))
b=2+5j
print(abs(b)) #5.385164807134505 输出模长

c=5
d=3
print(divmod(c,d)) #(1,2)

print(2,3)#8

print(round(5.23)) #2
print(round(5.2367,2))#5.24 后面的这个参数2表示保留小数点后2位

"""
all(x)	组合类型变量 x 中所有元素都为真时返回 True，否则返回 False；若 x 为空，返回 True。
any(x)	组合类型变量 x 中任一元素为真时返回 True，否则返回 False；容器 any([]) 返回 False）
reversed(r)	返回组合类型 r 的逆序形式（迭代器）。
sorted(x)	对组合数据类型 x 进行排序，默认从小到大，返回新列表。
sum(x)	对组合数据类型 x 计算求和结果。
"""
ls=[True,True,2] #一个数值，只要不是0，翻译成bool类型就是True
print(all(ls))

ls=[]
print(all(ls)) #返回True

print(any(ls)) #Faluse

ls=[True,True,0] 
print(any(ls)) #True

ls=[1,23,3445,5,2,45]
print(reversed(ls)) #<list_reverseiterator object at 0x03BB1AD0>
print(list(reversed(ls))) #此处做一个强制转换成list [45, 2, 5, 3445, 23, 1]

print(sorted(ls)) #[1, 2, 5, 23, 45, 3445]

print(sum(ls)) #3521

"""
eval(s)	计算字符串 s 作为 Python 表达式的值。——去除字符左右的字符串
exec(s)	执行字符串 s 作为 Python 语句（无返回值）。
range(a, b, s)	从 a 到 b（不包含 b）以 s 为步长产生一个整数序列（迭代对象）。
"""
ls="[1,2,3,56]"
print(type(ls)) #<class 'str'>
print(eval(ls))#[1, 2, 3, 56]
print(type(eval(ls))) #<class 'list'>


score=eval(input("请输入你的成绩："))
print(score)
print(type(score))


value=123
a=eval("value")
print(a)#123

exec("a=1+999")
print(a) #1000

for i in range(10):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,101,2):
    print(i)
