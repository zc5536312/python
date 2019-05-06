#导入所需的模块
from tkinter import *
import time
import random

tk=Tk()                         #创建Tk窗口实例
tk.title("弹球游戏")            #为窗口取名 

canvas=Canvas(tk,width=800,height=600,bg="skyblue",bd=0,highlightthickness = 0) #设置窗口大小、背景颜色以及边框厚度
tk.resizable(0,0)               #设置窗口大小无法被鼠标拉伸或缩小
canvas.pack()                   #通知窗口管理器注册其组件
tk.update()                     #刷新窗口

#预设置文本大小、文本内容、文本类型以及状态
#游戏开始、暂停；游戏结束；游戏总得分
game_startsigal_text=canvas.create_text(70,10,text='DOWN: START',font=('Times',15),state='hidden')
game_endsigal_text=canvas.create_text(65,30,text='UP: TimeOut',font=('Times',15),state='hidden')
game_over_text=canvas.create_text(430,200,text='GAME OVER',font=('Times',30),state='hidden')
game_start_text=canvas.create_text(430,110,text='GAME START',font=('Times',20),state='hidden')
game_score_text=canvas.create_text(430,60,text='SCORE:',font=('Times',15),state='hidden')

#定义小球类
class Ball:
        def __init__(self,canvas,paddle,color):
                self.canvas=canvas
                self.paddle=paddle
                self.id=canvas.create_oval(10,10,25,25,fill=color)              #小球颜色与大小，直径为15
                self.canvas.move(self.id,400,100)                               #小球初始位置
                stat=[-3,-2,-1,1,2,3]                                           #随机数设置初始小球的水平方向速度，竖直方向保持为-3
                random.shuffle(stat)
                self.x=stat[0]
                self.y=-3
                self.canvas_height=self.canvas.winfo_height()
                self.canvas_width=self.canvas.winfo_width()
                self.hit_bottom=False
        def hit_paddle(self, pos):                                              #获取球的坐标，并判断是否击中板子
                paddle_pos = self.canvas.coords(self.paddle.id )
                if pos[2]>= paddle_pos[0] and pos[0]<= paddle_pos[2]:
                        if pos[3]>= paddle_pos[1] and pos[3]<= paddle_pos[3]:
                                return True
                return False
        def draw(self):                                                         #绘制球的所在位置
                self.canvas.move(self.id,self.x,self.y)
                pos=self.canvas.coords(self.id)
                if pos[3]>=self.canvas_height:
                    self.hit_bottom=True
                if self.hit_paddle(pos)==True:                                  #撞击板后反弹，竖直速度为-4，且积分器+1
                     self.y=-4
                     score.addscore()
                if pos[0]<=0:                                                   #撞击边界后，水平和竖直方向速度反向，大小设置为2      
                     self.x=2
                if pos[1]<=0:
                     self.y=2
                if pos[2]>=self.canvas_width:
                     self.x=-2
                if pos[3]>=self.canvas_height:
                     self.y=-2
#定义板子类
class Paddle:
        def __init__(self,canvans,color):
            self.canvas=canvas
            self.id=canvas.create_rectangle(0,0,150,10,fill=color)              #设置板子大小和颜色
            self.canvas.move(self.id,400,450)                                   #设置板子初始位置
            self.started=False                                                  #初始状态：未开始
            self.x=0                                                            #初始速度为0
            self.canvas_width=self.canvas.winfo_width()                      
            self.canvas.bind_all("<KeyPress-Left>",self.turn_left)              #设置上下左右按键的功能，左右控制方向，上表示暂停，小表示开始游戏
            self.canvas.bind_all("<KeyPress-Right>", self.turn_right)
            self.canvas.bind_all("<KeyPress-Down>", self.game_start)
            self.canvas.bind_all("<KeyPress-Up>", self.game_stop)
        def turn_left(self,event):                                              #左右按键改变板子的速度方向，大小为3
                self.x=-10 
                '''
                t = int(time.time())
                
                while t!=0:   #无限循环...     
                        self.x=-3
                        print(int(time.time()))
                        if int(time.time()) == int(t+2):
                                self.x=-3 
                                print("1")             
                                break

               '''
        def turn_right(self,event):
                self.x=10
                '''
                t = int(time.time())
                
                while t!=0:   #无限循环...     
                        self.x=3
                        print(int(time.time()))
                        if int(time.time()) == int(t+2):
                                self.x=3   
                                print("1")          
                                break
               '''
        def game_start(self,evt):                                               #开始
                self.started=True
        def game_stop(self,evt):                                                #暂停
                self.started = False
        def draw(self):                                                         #绘制板子，到达两端时设置速度为0
                self.canvas.move(self.id,self.x,0)
                pos=self.canvas.coords(self.id)
                if pos[0]<=0:
                        self.x=0
                if pos[2]>=self.canvas_width:
                        self.x=0
               
#定义积分器类
class Score:                                                                    #功能：显示分数和显示操作提示
    def __init__(self,canvas,color):
        self.score=0;                                                           #初始化分数为0分
        self.canvas=canvas
        canvas.itemconfig(game_score_text, state='normal')
        self.id=canvas.create_text(470,60,text=self.score,fill=color)           #设置分数的位置和颜色，分数的大小会随着得分的越高而越大
        
        canvas.itemconfig(game_startsigal_text, state='normal')                 #将UP、DOWN按键的操作提示显示在窗口中
        canvas.itemconfig(game_endsigal_text, state='normal')
        
    def addscore(self):                                                         #积分器+1，刷新并显示到窗口
        self.score+=1
        self.canvas.itemconfig(self.id,text=self.score)

#创建板子、球和积分器类
paddle=Paddle(canvas,"yellow")
ball=Ball(canvas,paddle,"red")
score=Score(canvas,'black')

#主程序运行
while 1:                                                                        #画布一出现会马上消失，为了防止画布消失，用tkinter一直重画
        if ball.hit_bottom==False and paddle.started==True:
                ball.draw()
                paddle.draw()
                canvas.itemconfig(game_start_text, state='normal')              #显示game start字符串
        
        if ball.hit_bottom==True:                                               #到达窗口底部，显示“game over”，“game start”字符串隐藏
                canvas.itemconfig(game_over_text, state='normal')
                canvas.itemconfig(game_start_text, state='hidden')
        tk.update_idletasks()
        tk.update()                                                             #刷新窗口
        time.sleep(0.01)                                                        #sleep0.01秒，再计算下一步小球和板子的位置

