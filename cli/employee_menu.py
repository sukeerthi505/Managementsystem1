from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB

#this is an object for employee repo
emp_db=EmployeeDB()
#this is an object for employee auth
emp_auth=EmployeeAuthentication(emp_db)


def employeeSignup():
    print('Employee signup')
    name=input('enter your name:')
    email=input('enter your email:')
    password=input('enter your password:')
    emp_auth.createEmployee(name,email,password)
    
def employeeLogin():
    print('Employee Login')https://github.com/sukeerthi505/Managementsystem1
