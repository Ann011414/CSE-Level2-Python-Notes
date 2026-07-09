### 序列类型可以存储有序且可以重复的数据：列表（list） 元组（tuple）

# list []
ls=[123,123,3.14,"abc","abc"]
print(ls)
print(type(ls))
# 列表索引： 索引用来表示列表中元素的所在位置  一个列表中有n个元素，索引取值范围是0-n-1
print(ls[0]) #和字符串索引一样
print(ls[::-1])

l2=[123,234,[12,3,4],[45,13]]
print(l2)
print(l2[2])
print(l2[2][2]) #可以在列表中存储列表，还可以嵌套的索引

## 常用的操作符与函数
ls=[123,321,456,3.14]
print(len(ls))
print(123 in ls)
print(123 not in ls)
print(min(ls))
print(max(ls)) # 注意此处 如果列表中有字符串之类的，则会报错

strls=['aa','ab','c','d','e']
print(max(strls))
print(min(strls)) #但是如果都是字符串，就可以输出；按照字母序靠后的更大的顺序


##常用操作方法
"""
ls.append (x)：在列表 ls 末尾添加一个新元素 x
ls.insert (i,x)：在列表 ls 第 i 位增加元素 x
ls.clear ()：清空列表 ls 中所有元素
ls.pop (i)：将列表 ls 中第 i 个元素删除
ls.remove (x)：将列表中出现的第一个元素 x 删除
ls.reverse ()：将列表 ls 中的元素反转
ls.index (x)：返回列表 ls 中第一次出现元素 x 的位置
ls.count (x)：统计列表 ls 中出现 x 的总次数
ls.copy ()：返回一个新列表，复制 ls 中所有元素
"""
ls=list() # list([])
print(ls,type(ls))
ls=[] #这样也行

ls.append(123)
ls.append("hello")
print(ls)

ls.insert(1,"world")
print(ls)

ls.pop(0) #如果不指定参数，就默认删除最后面的元素
print(ls)

ls.remove("hello")
print(ls) #这个remove是相对于元素的删除，必须要有这个元素才能删除（否则报错）

#--------------------------------------------------------------------
ls=[123,234,3.14,65,"abc","helloworld"]

#ls.reverse()
#print(ls)

print(ls.index(123))

print(ls.count(123))

ls.clear()
print(ls)

"""
易错！！！copy
"""
a=[123,234,567]
b=a #此时 a&b 都是指向同一个列表
b[1]=3.14  #此处用索引改变了b的值
print(a)
print(b) #此时居然发现 a 和b 的输出居然是一样的？？？

a=[123,234,567]
b=a.copy() #如果此时使用这个copy方法！！！
b[1]=3.14  
print(a)
print(b)
"""
此时output:
[123, 234, 567]
[123, 3.14, 567]
"""
#======================================================================
#======================================================================

"""
元组 tuple
一旦定义就不能修改！！！
使用()来表示
元组的索引和切片和列表完全一致
"""
t=(123,3.14,123,"abc")
print(t)
print(type(t))
print(t[0:3])

#----------------------------------------------------------------------
#列表和循环for的组合
ls=[123,234,"abc"]
for i in ls:
    print(i)

t=(123,234,"abc")
for i in t:
    print(i)














