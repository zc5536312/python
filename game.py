from tkinter import *
import time 

t = int(time.time())
print(t)
                
while t!=0:   #无限循环...     
        print(int(time.time()))
        
        if int(time.time()) == int(t+2):
                print("1")           
                break


print(t+2)