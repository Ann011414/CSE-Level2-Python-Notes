"""
一维数据：一行数据
二维数据：Excel表格中的那种数据
高位数据：多层嵌套的数据
"""
###一维数据
ls=["北京","上海","深圳"]
print(ls)
s=",".join(ls)
print(s) #北京,上海,深圳

#CSV 文件——默认用逗号分隔存储的内容（就是一个Excel表格，行之间的内容用逗号分隔
f=open("city.csv","w")
f.write(s) #注意write只能写入字符串，直接把list写入会报错
f.close()

f=open("city.csv","r")
info=f.read()
f.close()
print(info) #北京,上海,深圳
ls=info.split(',')
print(ls) #['北京', '上海', '深圳']

###二维数据
students=[
          ["学号","姓名","性别","年龄"],
          ["1001","张三","男","17"],
          ["1002","李四","男","18"],
          ["1003","王五","男","19"],
          ["1004","赵六","女","20"],
    ]
print(students[0][1])
for s in students:
    print(s)
"""
输出：
['学号', '姓名', '性别', '年龄']
['1001', '张三', '男', '17']
['1002', '李四', '男', '18']
['1003', '王五', '男', '19']
['1004', '赵六', '女', '20']
"""

for s in students:
    for i in s:
        print(i)
"""
学号
姓名
性别
年龄
1001
张三
男
17
1002
李四
男
18
1003
王五
男
19
1004
赵六
女
20
"""
## 这是写一个二维文件
f=open("students.csv","w")
for row in students:
    f.write(",".join(row)+"\n")
f.close()

## 这是读出一个二维文件
f=open("students.csv","r")
for line in f:
    print(line)
"""
学号,姓名,性别,年龄

1001,张三,男,17

1002,李四,男,18

1003,王五,男,19

1004,赵六,女,20
"""
f.close()

f=open("students.csv","r")
student=[]
for line in f:
    line=line.strip("\n") #去除换行符
    """
    删掉字符串两头指定的字符（这里是换行符 \n）
    CSV 文件每一行末尾都会自带换行符 \n（回车换行标记），
    比如原始字符串："1001,张三,男,20\n"
    strip("\n") 会把开头和结尾的 \n 全部删掉，变成干净字符串："1001,张三,男,20"
    通用写法：line.strip()（不带参数 = 删除两端所有空白：换行符\n、空格、制表符\t，更推荐）
      比如
      s = "  abc,123\n"
      s = s.strip()
      print(s)  # 结果："abc,123"  去掉前后空格和换行
    """
    temp=line.split(",")#这是在拆
    print(temp)
    student.append(temp) #这是把他放在一个大列表student中
f.close()
print(student) #[['学号', '姓名', '性别', '年龄'], ['1001', '张三', '男', '17'], ['1002', '李四', '男', '18'], ['1003', '王五', '男', '19'], ['1004', '赵六', '女', '20']]

    
    
