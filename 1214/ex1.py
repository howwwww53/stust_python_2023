class Student:
    def __init__(self,name,id,major):
        self.name=name
        self.id=id
        self.major=major

    def studentname(self):
        print(self.name,self.id,self.major)

    def add(self,course):
        self.course=course
        print("{}選了[{}]".format(self.name,course))   

    def retreat(self,retreat):
        if(self.course==retreat):
            print("{}退選[{}]".format(self.name,retreat))

            
   


obj1=Student("Big A","s001","資工")
obj2=Student("Big B","s002","電機")

obj1.add("國防")
obj2.add("程式設計")
obj1.retreat("國防")
            