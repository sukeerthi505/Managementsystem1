from getpass4 import getpass
from dotenv import load_dotenv
import os
from services.auth import AdminAuthentication 
from repositories.employee_repo import EmployeeDB
from repositories.manager_repo import ManagerDB
from repositories.request_repo import RequestDB
from services import admin_services

emp_db = EmployeeDB()
mgr_db = ManagerDB()
req_db = RequestDB()
admin_auth = AdminAuthentication(emp_db,mgr_db,req_db)

load_dotenv()

def adminWelcome():
    print('Welcome back Admin')

def adminLogin():
    password = getpass('Enter your password:')
    if password == os.getenv('ADMIN_PW'):
        adminWelcome()
        adminMainMenu()
    else:
        print('password is incorrect try to login again')
        adminLogin()

def managerPromotion():
    id = int(input('Enter the employee id to promote to manager:'))
    data = admin_auth.db.getEmp(id)
    if data[5] == 0:
        if data is not None:
            admin_auth.db.modifyEmptoMgr(id)
            adminMainMenu()
        else:
            print(f'employee with id {id} is not present enter the id again')
            managerPromotion()
    else:
        print(f'employee with id {id} is already a manager try with some other employee id')
        managerPromotion()

def adminMainMenu():
    choice = int(input('''
_____________________________________________________
|press 1 for all employee data#                     |
|press 2 for all manager data#                      |
|press 3 for promote employee to manager#           |
|press 4 for assign project to manager              |
|press 5 for see the manager requests for employee  |
|press 6 for assign employee to manager             |
|press 7 for check the update of the project        |
|press 8 for logout                                 |
|___________________________________________________|
enter your choice:'''))

    if choice == 1:
        emp_datas = admin_auth.db.getAllEmp()
        for emp_data in emp_datas:
            print(f'''
__________________________________
employee id : {emp_data[0]}
employee name : {emp_data[1]}
employee email: {emp_data[2]}
employee manager id: {emp_data[4]}
__________________________________''')
        adminMainMenu()
            
    elif choice == 2:
        mgr_datas = admin_auth.mgr_db.getAllMgr()
        for mgr_data in mgr_datas:
            print(f'''
__________________________________
manager id : {mgr_data[0]}
manager name : {mgr_data[1]}
manager email: {mgr_data[2]}
__________________________________''')
        adminMainMenu()

    elif choice == 3:
        managerPromotion()

    elif choice == 4:
        pass
    elif choice == 5:
        admin_services.seeMgrReq(admin_auth)
        adminMainMenu()
    elif choice == 6:
        pass
    elif choice == 7:
        pass
    elif choice == 8:
        return
    else:
        print('Enter the correct option')
        adminMainMenu()

    