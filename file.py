import win32ui
 
dlg= win32ui.CreateFileDialog(0)# 1表示打开文件对话框
dlg.SetOFNInitialDir('E:/Python')# 设置打开文件对话框中的初始显示目录
dlg.DoModal()
 
filename= dlg.GetPathName()# 获取选择的文件名称







