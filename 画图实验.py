import matplotlib.pyplot as plt
import numpy as np

# x = np.arange(3,9,1)    #x轴数据
# y1 = x*2
# y2 = x**2
# plt.figure(figsize=(5,3.5))
# plt.plot(x, y1,'y',marker='o',label='y1:double x')  #关键句,前两个参数是X、Y轴数据,其他参数指定曲线属性，如标签label，颜色color,线宽linewidth或lw,点标记marker
# plt.plot(x,y2,'b',marker='^',label='y2:square of x')
# plt.legend(loc='best')  #显示图例，前提是plot参数里写上label;loc是图例的位置
# plt.xlabel('x(ms)')
# plt.ylabel('y')
# plt.title('a simple example')
# #plt.savefig('G:/YDPIC/example.png',dpi=80)  #除了png，还有一些格式如svg，dpi是dot per inch每英寸的像素点数，缺省值80，论文写作一般要求1200或者矢量图
# plt.show()  #show函数显示图表会中断程序，直到关闭图像。不要把show写在savefig前，否则保存图像一片空白。最好是注释掉savefig或者show其中一行。



data_matrix = np.zeros((3, 8))

print(data_matrix)