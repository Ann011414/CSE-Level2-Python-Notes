### pip的使用
"""
pip 工具使用
pip <命令> <选项>
安装：install 库名
卸载：uninstall 库名
下载：download 库名
查看当前第三方库列表：list
查看某个第三方信息：show <库名>
"""
import jieba
print(jieba.lcut("国家计算机二级考试"))

#------------------------------------------------------------------

### jieba（“结巴”）是 Python 中一个重要的第三方中文分词函数库，能够将一段中文文本分割成中文词语的序列，jieba 库需要通过 pip 指令安装。
"""
jieba.lcut(s)	精确模式，返回一个列表类型
jieba.lcut(s, cut_all=True)	全模式，返回一个列表类型
jieba.lcut_for_search(s)	搜索引擎模式，返回一个列表类型
jieba.add_word(w)	向分词词典中增加新词 w
"""
ls=jieba.lcut("国家计算机二级考试Python学科")
print(ls)

ls=jieba.lcut("国家计算机二级考试Python学科",cut_all=True)
#这是找到所有可能的分词
print(ls)

ls=jieba.lcut_for_search("国家计算机二级考试Python学科")
print(ls)
#['国家', '计算', '算机', '计算机', '二级', '考试', 'Python', '学科']
#这是“搜索模式”，比上面的全模式出来的要少一些

jieba.add_word("Python学科")
ls=jieba.lcut("国家计算机二级考试Python学科")
print(ls) #['国家', '计算机', '二级', '考试', 'Python学科']
#相当于指定“Python学科”为一个词

#--------------------------------------------------------------------

### Python常见第三方库
"""
网络爬虫方向
requests	简洁且简单处理 HTTP 请求
scrapy	Web 获取框架，一个半成品爬虫


数据分析方向
numpy	科学计算库
scipy	在 numpy 基础上增加了很多库函数
pandas	数据处理、数据分析


文本处理方向
pdfminer	读取 pdf 数据
openpyxl	处理 Excel 表格
python-docx	处理 word 文档
beautifulsoup4	解析和处理 HTML、XML


数据可视化方向
matplotlib	二维图绘制
TVTK	三维可视化
mayavi	更方便的三维可视化


用户图形界面方向
PyQt5	用户图形界面开发
wxPython	用户图形界面开发
PyGTK	用户图形界面开发


机器学习方向
scikit-learn	机器学习
TensorFlow	人工智能
Theano	深度学习


Web 开发方向
Django	Web 框架
Pyramid	Web 框架
Flask	Web 框架


游戏开发方向
Pygame	多媒体制作
Panda3D	3D 引擎
cocos2d	2D 引擎


其它第三方库
PIL	图像处理
SymPy	数学计算
NLTK	自然语言处理
WeRoBot	微信机器人框架
MyQR	二维码
"""
