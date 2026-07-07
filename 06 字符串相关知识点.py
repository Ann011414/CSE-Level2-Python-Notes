#常用的字符串操作符
s1="hello"
s2="world"
print(s1+s2)
print(s1*5)

#in 运算符 判断一个字符串是不是在另一个字符串里面
s1="how are you doing"
print("how" in s1)
s2="yo"
print(s2 in s1)

## 字符串的索引
s= "how are you doing"
print(s[0])
print(s[3]) #这个是空格

### 字符串切片：<字符串或字符串变量>（开始索引：结束索引：步长）
# 注意，不包含结束索引的位置
s="how are you doing"
print(s[1:6])
print(s[1:]) #从第一个索引到最后
print(s[:8]) #注意这个不包含第8个索引的位置
print(s[:]) #这个是取全部
#s=s[1:4] #这个是改变了s字符串的内容

#关于步长
print(s[0:11:1])
print(s[0:11:2])
print(s[::-1]) #这个是逆序排列

print(s[-1]) #这个是说输出倒数第一位
print(s[:-2]) #这个是说最后是第-2位（不包含第-2位）




###字符串常用函数
# len
s= "hello"
print(len(s))
# str
a=123
a=str(a)
print(type(a))

# chr: 把 unicode 编码变成字符
print(chr(97))


# ord  和chr 效果相反 把字符变成unicode 编码
print(ord("a"))


#hex
print(hex(20))  #这是变成16进制

#oct
print(oct(20))  #这是变成8进制



### 字符串处理方法——这个方法和“函数”的区别是，必须要已有一个字符串str 然后 . 然后可以用

s1="How ARE YOU DOING"
s2="how are you doing"

print(s1.lower())  # 这是返回字符串s1的副本，全部字符小写（小写的依然小写）
print(s1)

print(s2.upper())  #这是把字母全部变成大写

# split  这是把字符串拆开，变成列表！！  （默认用“空格”分开）
s="sddf-djoja-ebji-dsjoiew"
a=s.split(sep="-")  #此处也可以直接写 s,split("-")
print(a)

names="张三 李四  王五"
print(names.split())


#str.count(sub,start,end) 计算子串在str中出现的次数，后两个是可选参数
s="abc3493abc498abc038abc"
print(s.count("abc"))


# str.replace(old,new) 返回字符串的副本 所有old子串替换成new
s1="HelloWorld"
s2=s1.replace("o","O") #此处把小写的o替换成大写的O
print(s1,s2)

#str.center(width,fillchar) 可能不太用，但是考试要考！！！
s="hello"
print(s.center(10,"="))  #输出 ==hello===
print(s.center(10))  #输出  hello   即不指定fillchar则自动用空格填充
print(s.center(2)) #输出hello 即如果width小于原字符串，就不做处理


# str.strip(chars) 从字符串str中去掉其左侧和右侧chars中列出的字符
s1="  python  "
print(s1.strip())  #如果不写参数，默认参数是空格

s2="==python=="
print(s2.strip("=="))  #输出python

s3=" ==python== "
print(s3.strip("==")) #输出 ==python== 因为左右两边并非==而是空格


#str.join(iter)  特别好用！！！！！！
print(",".join("python"))  #output p,y,t,h,o,n


#capitalize()  把第一个首字母变成大写
s="hello world group select.i am daidai"
print(s.capitalize())

#index(sub,begin,end)返回sub在当前字符串中第一次出现的位置，如果没找到，报错
#find(sub,begin,end)返回sub在当前字符串中第一次出现的位置，如果没找到，返回-1
"""
这两个函数只是在返回值上有不同，其他的都一样；其中begin 和end 是可选参数
"""
s="I was thinking of taking you somewhere special for dinner tonight"
print(s.index("o"))
print(s.find("o")) #都是输出15
print(s.index("o",16))
print(s.find("o",16))
print(s.find("o",16,20))



