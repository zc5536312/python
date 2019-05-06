from PIL import Image
import os
import time

import win32ui

def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')

path=GetDesktopPath()

 
dlg= win32ui.CreateFileDialog(1)# 1表示打开文件对话框
dlg.SetOFNInitialDir(path)# 设置打开文件对话框中的初始显示目录
dlg.DoModal()
 
filename= dlg.GetPathName()# 获取选择的文件名称
#print filename


t1=int(time.time())
print(t1)
t2=str(t1)+".jpg"
 
infile = dlg.GetPathName()# 获取选择的文件名称
outpath = r"C:\Users\Administrator.DESKTOP-PHEFBL0\Desktop\z1.jpg"
im = Image.open(infile)
im.show()
(x,y) = im.size
y_s = int(y * 700 / x )
smallimg=im.resize((700,y_s),Image.ANTIALIAS)
smallimg.save(t2)
 
