class Employee:
    #Over riding method  
    def message(self):
        print('This message is from Employee Class')
  
class Department(Employee):
  
    def message(self):
        print('This Department class inherited from Employee')
 

class Sales(Employee):
  
    def message(self):
        print('This Sales class is also inherited from Employee')
         
emp = Employee()
emp.message()
  
print('------------')
dept = Department()
dept.message()
 

print('------------')
sl = Sales()
sl.message()
