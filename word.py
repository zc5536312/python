import win32com
from win32com.client import Dispatch, constants
wordApp = win32com.client.Dispatch('Word.Application')

# 后台运行，显示，不警告
wordApp.Visible = True
wordApp.DisplayAlerts = 0

# 创建新的文档
doc = wordApp.Documents.Add() 

# 插入文字
doc.Paragraphs.Last.Range.Text = 'hello!'

# 保存文件
doc.SaveAs('d://say_hello.docx')