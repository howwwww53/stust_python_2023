class chicken:
    def __init__(self,name,taste,drink,guestname,finish):
        self.name=name
        self.taste=taste
        self.drink=drink
        self.guestname=guestname
        self.finish=finish



    def chickenname(self):
        x = input("請輸入 台式，韓式，美式，泰式，唐揚:: ")
        self.name = x  #用x輸入值回傳 
     
  
    def printchicken(self):
        print(self.name,self.taste,self.drink,self.guestname,self.finish)  #輸出所有

    def chosetaste(self):
        x=input("請輸入 原味，勁辣::") 
        self.taste=x   #用x輸入值回傳兩種口味

    def chosedrink(self):
        x=input("請輸入 可樂，雪碧，紅茶，綠茶::")
        self.drink=x    #用x輸入值回傳四種飲品      

    def inputguestname(self):
        x=input("請輸入大名::")
        self.guestname=x #用x輸入值回傳大名
   

    



#4個物件
no1=chicken("","","","","訂單送出")
no2=chicken("","勁辣","","","訂單送出")
no3=chicken("","","雪碧","","訂單送出")
no4=chicken("美式","","","","訂單送出")

#呼叫副函示
no1.chickenname()
no1.chosetaste()
no1.chosedrink()
no1.inputguestname()
no1.printchicken()

no2.chickenname()

no2.chosedrink()
no2.inputguestname()
no2.printchicken()


no3.chickenname()
no3.chosetaste()

no3.inputguestname()
no3.printchicken()



no4.chosetaste()
no4.chosedrink()
no4.inputguestname()
no4.printchicken()

