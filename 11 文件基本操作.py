"""
文件的类型
1、文本文件（就是打开之后可以直接看到可识别的文字的哪些文件，比如txt）
由单一特定编码的字符组成
2、二进制文件（如mkv视频或者png图片）
直接由0和1组成，没有统一的字符编码

区别：是否有统一的字符编码

文件的操作
打开文件open()——读或者写——关闭文件close()
"""
###打开文件
#<变量名>=open(<文件路径及文件名>,<打开模式>)
"""
'r'：只读模式，如果文件不存在，返回异常 FileNotFoundError，默认值
'w'：覆盖写模式，文件不存在则创建，存在则完全覆盖原文件
'x'：创建写模式，文件不存在则创建，存在则返回异常 FileExistsError
'a'：追加写模式，文件不存在则创建，存在则在原文件最后追加内容
'b'：二进制文件模式
't'：文本文件模式，默认值
'+'：与 r/w/x/a 一同使用，在原功能基础上增加同时读写功能

文件的操作 - 常用组合
以文本方式只读打开一个文件，读入后不能对文件进行修改：r
以文本方式可读写地打开一个文件，可以读入并修改文件：r+
以文本方式打开一个空文件，准备写入一批内容，并保存为新文件：w
以文本方式打开一个空文件或已有文件，追加形式写入一批内容，更新原文件：a+
以二进制方式只读打开一个文件，读入后不能对文件进行修改：rb
"""
"""
文件的操作—读
f.read (size)：从文件中读入整个文件内容。参数可选，如果给出，读入前 size 长度的字符串或字节流
f.readline (size)：从文件中读入一行内容。参数可选，如果给出，读入该行前 size 长度的字符串或字节流
f.readlines (hint)：从文件中读入所有行，以每行为元素形成一个列表。参数可选，如果给出，读入 hint 行
f.seek (offset)：改变当前文件操作指针的位置，offset 的值：0 为文件开头；1 为从当前位置开始；2 为文件结尾
"""

f=open("test_11.txt","rt",encoding="utf-8") #windows对中文的编码模式是GBK 但是Python的字符编码是Unicode，也叫UTF-8
#注意这个代码需要读取的文件和这个代码保存在同一个文件夹里面
s=f.read()
f.close()
print(s)


#相对路径
path="testFile/test_11_2.txt"
#绝对路径
path="D:/IDLE练习/testFile/test_11_2.txt"
file=open(path,"rt",encoding="utf-8") 
s_open=file.read()
file.close()
print(s_open)

#注意上面的斜杠的方向，如果是反斜杠，就是转义字符
"""
\n   换行
\t   tab
\\   \
"""
#---------------------------------------------------------------------------

### 文件的读操作
path="test_11.txt"
f=open(path,"r",encoding="utf-8")
s=f.read()
print(s)
f.close()

f=open(path,"r",encoding="utf-8")
s=f.read(4) #output:大家好，
print(s)
f.close()

f=open(path,"rb") #这个是二进制文件模式
s=f.read(4) #output:b'\xe5\xa4\xa7\xe5'
print(s)
f.close()

f=open(path,"r",encoding="utf-8")
s=f.readline() #默认只读一行,输出“大家好，”
print(s)
s=f.readline() #默认只读一行,输出“欢迎大家学习Python二级考试” 且与上面的print输出的内容空了一行
print(s)
f.close()

f=open(path,"r",encoding="utf-8")
s=f.readlines() #output:['大家好，\n', '欢迎大家学习Python二级考试'] 是以行为元素的一个列表
print(s)
f.close()

f=open(path,"r",encoding="utf-8")
s=f.readlines(1) #output:['大家好，\n']
print(s)
f.close()

























