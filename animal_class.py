class Dog(object):
    def __init__(self,name,age,color):
        self.name=name
        self.__age=age
        self.color=color
    def run(self):
        print(self.name,"跑啊！")
    def getage(self):
        return(self.__age)
dog1=Dog("大黄",18,"1")

dog1.run()
#print(dog1.age)
print(dog1.getage())