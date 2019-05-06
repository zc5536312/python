import hashlib
import random
import re
import time


import requests
from googletrans import Translator
from openpyxl import Workbook, load_workbook
from openpyxl.writer.excel import ExcelWriter



import win32ui
 
dlg= win32ui.CreateFileDialog(1)# 1表示打开文件对话框
dlg.SetOFNInitialDir('E:/Python')# 设置打开文件对话框中的初始显示目录
dlg.DoModal()
 
filename= dlg.GetPathName()# 获取选择的文件名称

wb = load_workbook(filename)

list1 = wb.get_sheet_names()

i = len(list1)



for a1 in range(0, i):
   sheet = wb.get_sheet_by_name(list1[a1])
   print("打印" + str(list1[a1]))

   for row in sheet.rows:
      for cell in row:
            if cell.value != None:
               c1 = cell.value
               if type(c1) == str and c1 != "-":   
                  i = str(int(time.time()*1000)+random.randint(1,10))

                  t = str(c1)
                  u = 'fanyideskweb'
                  l = 'aNPG!!u6sesA>hBAW1@(-'
                  src = u + t + i + l    
                  m2 = hashlib.md5()
                  m2.update(src.encode())
                  str_sent = m2.hexdigest()

                  head = {
                     'Accept':'application/json, text/javascript, */*; q=0.01',
                     'Accept-Encoding':'gzip, deflate',
                     'Accept-Language':'zh-CN,zh;q=0.9',
                     'Content-Length':'200',
                     'Connection':'keep-alive',
                     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                     'Host':'fanyi.youdao.com',
                     'Origin':'http://fanyi.youdao.com',
                     'Referer':'http://fanyi.youdao.com/',
                     'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36',
                     'X-Requested-With':'XMLHttpRequest',
                     # 'Cookie': 'YOUDAO_MOBILE_ACCESS_TYPE=1; OUTFOX_SEARCH_USER_ID=833904829@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1846816080.1245883; fanyi-ad-id=39535; fanyi-ad-closed=1; JSESSIONID=aaaYuYbMKHEJQ7Hanizdw; ___rl__test__cookies=1515471316884'
                  }
                  head['Cookie'] = 'OUTFOX_SEARCH_USER_ID=833904829@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=1846816080.1245883;  ___rl__test__cookies='+str(time.time()*1000)
                                 # '___rl__test__cookies=1515471316884'

                  data = {
                     'i': t,
                     'from':'AUTO',
                     'to':'AUTO',
                     'smartresult':'dict',
                     'client':'fanyideskweb',
                     'salt':i,
                     'sign':str_sent,
                     'doctype':'json',
                     'version':'2.1',
                     'keyfrom':'fanyi.web',
                     'action':'FY_BY_REALTIME',
                     'typoResult':'false'
                  }
                  try:
                     s = requests.session()
                  
                     url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
                     p = s.post(url,data= data,headers = head)
                     print(t)
                     pat=r'{"tgt":"(.*?)",'
                     result=re.findall(pat,p.text)
                     print(result[0])
                     cell.value=result[0]
                     time.sleep(1)

                  except Exception as e:
                     print(e)
                
               if type(c1) == int:  
                  
                  cell.value=cell.value
                  
   print("done")         
      
dlg2= win32ui.CreateFileDialog(0)# 1表示打开文件对话框
dlg2.SetOFNInitialDir('E:/Python')# 设置打开文件对话框中的初始显示目录
dlg2.DoModal()
 
filename2= dlg.GetPathName()# 获取选择的文件名称            
          

wb.save(str(filename2)+'.xlsx')
print("ok")
