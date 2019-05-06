#import win32ui
import os
from os import walk

import win32com
from win32com.client import Dispatch, constants

wdFormatPDF = 17
wdFormatDocument = 0


def GetDesktopPath():
    return os.path.join(os.path.expanduser("~"), 'Desktop')


def docx2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".docx", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

def doc2pdf(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".doc", ".pdf"), FileFormat=wdFormatPDF)
    doc.Close()
    word.Quit()

#########################################
def pdf2docx(input_file):
    word = Dispatch('Word.Application')
    doc = word.Documents.Open(input_file)
    doc.SaveAs(input_file.replace(".pdf", ".docx"), FileFormat=wdFormatDocument)
    doc.Close()
    word.Quit()

#########################################
if __name__ == "__main__":
    print("作者:死肥宅")
    doc_files = []
    path=GetDesktopPath()+"\目标文件夹"
    directory = path
    os.path.exists(directory)
    if os.path.exists(directory):
        for root, dirs, filenames in walk(directory):
            for file in filenames:
                #x = input("模式1pdf转word，模式2word转pdf")

                
                #if x =="1":
                if file.endswith(".pdf") :
                    print("开始中")
                    try:
                        pdf2docx(str(root + "\\" + file))
                    except Exception as e:
                        print(e)
                    
                    print("-----")
                # elif file.endswith(".docx"):
                #     print("开始中")
                #     try:
                #         docx2pdf(str(root + "\\" + file))
                #     except Exception as e:
                #         print(e)
                #     print("-----")
                        
                # if x =="2":
                #     if file.endswith(".doc") :
                #         print("开始中")
                #         try:
                #             pdf2docx(str(root + "\\" + file))
                #         except Exception as e:
                #             print(e)
                pdf2docx(str(root + "\\" + file))       

        print("done")
        c1=input("完事了")
    else:
        c2=input("桌面不存在目标文件夹，请检查")