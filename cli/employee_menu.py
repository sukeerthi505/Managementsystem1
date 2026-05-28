from services.auth import EmployeeAuthentication
from repositories.employee_repo import EmployeeDB
from validation.email_validator import email_vali 
from validation.pass_validator import password_vali
from getpass4 import getpass
from utils.pass_hash import password_hasher,check_password
from .manager_menu import managerMainMenu

#this object of employee repo
emp_db = EmployeeDB()
#this is object of employee auth
emp_auth = EmployeeAuthentication(emp_db)

#this function for signup new employee
def employeeSignup():
    print('Employee Signup')
    name = input('Enter your name:')
    email = input('Enter your email:')
    verify_email = emp_db.searchEmp(email)
    if verify_email is None: 
        if email_vali(email=email) is not None:
            password = getpass('Enter your password:')
            confirm_pw = getpass('Enter your password again:')
            if password == confirm_pw:
                if password_vali(password):
                    password = password_hasher(password)
                    emp_auth.createEmployee(name,email,password)
                else:
                    print('''
password is not valid
password should be minimum lenght of 5
password should contain atleast uppercase character ex: A X H....
password should contain atleast special character ex: @ # % ^ * !.....
password should contain atleast one digits ex: 7 2 1 8...
''')
                    employeeSignup()
            else:
                print('password and confirm password both are not same')
                employeeSignup()
        else:
            print('''
email id is not valid!!!!!!
''')
            employeeSignup()
    else:
        print(f'account with this Email id {email} is already exist.Login')
        employeeLogin()
    

def employeeLogin():
    print('Employee Login')
    email = input('Enter your email:')
    password = getpass('Enter your password:')
    data = emp_auth.empLogin(email)
    hashed_pw = data[3]
    is_manager = data[5]
    if check_password(password,hashed_pw):
        if  is_manager == 1:
            print('Manager login successfull!!!!')
            managerMainMenu(data[0])
        else:
            print('employee login successfull')
    else:
        print('login failed')
