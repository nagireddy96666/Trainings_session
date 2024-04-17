class Employee:
    # Method is same for different classes we pass different arguments with in the class methods is called method overloading 
    def add(self, a, b):
        print('The Sum of Two = ', a + b)
  
class Department(Employee):
  
    def add(self, a, b, c):
        print('The Sum of Three = ', a + b + c)
         
emp = Employee()
emp.add(10, 20)
  
print('------------')
dept = Department()
dept.add(50, 130, 90)
