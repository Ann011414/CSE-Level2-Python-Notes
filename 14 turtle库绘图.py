### 

"""
窗体函数：开启一个窗口来放我画的图
turtle.setup(width, height, startx, starty)
width: 窗口宽度
height: 窗口高度
startx: 窗口与屏幕左侧距离（单位像素）
starty: 窗口与屏幕顶部距离（单位像素）

画笔转态函数
pendown()	放下画笔
penup()	提起画笔，与 pendown () 配对使用
pensize(width)/width()	设置画笔线条的粗细为指定大小
pencolor()	设置画笔的颜色
color()	设置画笔和填充颜色
begin_fill()	填充图形前，调用该方法
end_fill()	填充图形结束
filling()	返回填充的状态，True 为填充，False 为未填充
clear()	清空当前窗口，但不改变当前画笔的位置

画笔运动函数
forward(distance)	沿着当前方向前进指定距离
backward(distance)	沿着当前相反方向后退指定距离
right(angle)	向右旋转 angle 角度
left(angle)	向左旋转 angle 角度
goto(x, y)	移动到绝对坐标 (x, y) 处
setx(x)	修改画笔的横坐标到 x，纵坐标不变
sety(y)	修改画笔的纵坐标到 y，横坐标不变
setheading(angle)	设置当前朝向为 angle 角度
home()	设置当前画笔位置为原点，朝向东
"""
import turtle
import turtle as t
t.setup(600,600,10,20)

#前进 forward(distance) fd()
#后退 backward(distance) bk()
"""
t.forward(100)#海龟脑袋默认向右
t.bk(200)
t.backward(50)

t.left(90)
t.forward(100)
"""

for i in range(4):
    t.fd(100)
    t.left(90)

###画笔状态函数
t.pensize(2)#这个默认是1 同时这个函数等价于 t.width(3)
t.width(4)

#pencolor(颜色的单词)  或者  pemcolor((r,g,b))分别用0—1来分别表示三个参数
t.pencolor("blue")
t.pencolor((1,0,0))
t.pencolor((1,0.5,0))

t.color("red","blue") #前一个参数是设置画笔颜色，后一个是设置填充颜色
t.begin_fill()

for i in range(4):
    t.fd(100)
    t.left(90)
t.end_fill()

t.clear() #清理图片，然后不改变画笔位置

print(t.filling()) #False


"""
画笔状态函数
reset()	清空当前窗口，并重置位置等状态为默认值
screensize()	设置画布窗口的宽度、高度和背景颜色
hideturtle()	隐藏画笔
showturtle()	显示画笔
isvisible()	如果 turtle 可见，则返回 True
write(str, font=None)	输出 font 字体的字符串
"""
t.reset()#这是清空之后还重置位置并且状态回复默认值
t.hideturtle()
t.showturtle()

t.write("在画图")


# pendown() 和 penup()
t.setup(600,600,10,10)
t.fd(200)
t.left(90)
t.penup() # pu() up() 这两种写法也行
t.fd(20)
t.left(90)
t.pendown() #pd() down()
t.fd(200)

"""
画笔运动函数
circle(radius, e)	绘制一个指定半径 radius 和角度 e 的圆或弧形
dot(size, color)	绘制一个指定直径 size 和颜色 color 的圆点
undo()	撤销画笔的最后一步动作
speed()	设置画笔的绘制速度，参数为 0~10 之间
"""
t.circle(60,180)#这个默认是逆时针，如果是-60就是顺时针

#t.speed(20)
t.circle(60,steps=6)#这是画一个圆的内切六边形

t.goto(60,100) #这个是让画笔去到这个坐标，同时会带出一条线

t.setx(120)
t.sety(0)

t.setheading(90)#seth()也可以
t.seth(60)

t.home()

t.dot(30,"red")




