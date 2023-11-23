class Person:
    def __init__(self,emp_id, emp_name, emp_salary,emp_department):
        self.emp_id=emp_id
        self.emp_namer=emp_name
        self.emp_salary=emp_salary
        self.emp_department=emp_department
        #self.hour=hour
    
    def emp_assign_department(self):
        x=input("請輸入更改後部門:")
        self.emp_department=x

    def print_employee_details(self):
       print(self.emp_id,self.emp_namer,self.emp_salary,self.emp_department)

    def calculate_emp_salary(self):
        hour=int(input("Time:"))
        if hour>50:
            print("薪水:",self.emp_salary,"加薪後:",self.emp_salary+(hour-50)*(self.emp_salary/50),"\n")
        else:
            print("薪水:",self.emp_salary,"\n")

        
obj1=Person("ADAMS", "E7876", 50000, "ACCOUNTING")
obj2=Person("JONES", "E7499", 45000, "RESEARCH")
obj3=Person("MARTIN", "E7900", 50000, "SALES")
obj4=Person("SMITH", "E7698", 55000, "OPERATIONS")

obj1.emp_assign_department()
obj1.print_employee_details()
obj1.calculate_emp_salary()


obj2.print_employee_details()
obj2.calculate_emp_salary()

obj3.emp_assign_department()
obj3.print_employee_details()
obj3.calculate_emp_salary()


obj4.print_employee_details()
obj4.calculate_emp_salary()

