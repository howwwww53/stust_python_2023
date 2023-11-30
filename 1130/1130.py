class student:
    def __init__(self, school,department,chairname,name,id,address,credit,score):
        self.school=school
        self.department=department
        self.chairname=chairname
        self.name=name
        self.id=id
        self.address=address
        self.credit=credit
        self.score=score
    
    def getSchool(self):
        return self.school
    def setSchool(self,value):
        self.school=value

    def getdepartment(self):
        return self.department
    def setdepartment(self,value):
        self.department=value
        
    def getchairname(self):
        return self.chairname
    def setchairname(self,value):
        self.chairname=value

    def getname(self):
        return self.name
    def setname(self,value):
        self.name=value

    def getid(self):
        return self.id
    def setid(self,value):
        self.id=value

    def getaddress(self):
        return self.address
    def setaddress(self,value):
        self.address=value


    def getcredit(self):
        return self.credit
    def setcredit(self,value):
        self.chairname=value

    def getscore(self):
        return self.score
    def setscore(self,value):
        self.score=value

#建立物件
st1=student("STUST","CSIE","延鈺","洺豪","4B0G0134","高雄",120,90)
#呼叫副函式
print(st1.getSchool())
print(st1.getdepartment())
print(st1.getchairname())
print(st1.getname())
print(st1.getid())
print(st1.getaddress())
print(st1.getcredit())
print(st1.getscore())