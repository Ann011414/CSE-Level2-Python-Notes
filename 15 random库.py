### 实际上随机数并不是真的随机数，而是由种子生成的
"""
seed(a = None)	初始化随机数种子，默认值为当前系统时间
random()	生成一个 [0.0, 1.0) 之间的随机小数
randint(a, b)	生成一个 [a, b] 之间的整数
getrandbits(k)	生成一个 k 比特长度的随机整数
randrange(start, stop[, step])	生成一个 [start, stop) 之间以 step 为步长的随机整数
uniform(a, b)	生成一个 [a, b] 之间的随机小数
choice(seq)	从序列类型（例如列表）中随机返回一个元素
shuffle(seq)	将序列类型中元素随机排列，返回打乱后的序列
sample(pop, k)	从 pop 中随机选取 k 个元素，以列表类型返回
"""
from random import *
print(random())

seed(10)
print(random())

seed(10)
print(random())

print(randint(1,10))

print(randrange(10,100,2))

print(uniform(5,10))

ls=[12,23,34,2.34,34,94]
print(choice(ls))

shuffle(ls)
print(ls)

print(sample(ls,4))
