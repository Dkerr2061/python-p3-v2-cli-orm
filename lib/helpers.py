from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(f"Department {name} not found.")


def find_department_by_id():
    id_ = input("Enter the depratment's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f"Department {id_} not found.")


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f"Success {department}")
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter department's new name: ")
            department.name = name
            location = input("Enter department's new location: ")
            department.location = location
            department.update()
            print(f"Success {department}")
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f"Department {id_} not found.")



def delete_department():
    id_ = input("Enter department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f"Department {id_} deleted.")
    else:
        print(f"Department {id_} not found.")


# You'll implement the employee functions in the lab

def list_employees():
    employee = Employee.get_all()
    for employee in employee:
        print(employee)


def find_employee_by_name():
    name = Employee.find_by_name(name)
    print(name) if name else print(f"Employee {name} not found.")


def find_employee_by_id():
    id_ = Employee.find_by_id(id_)
    print(id_) if id_ else print(f"Employee {id_} not found.")


def create_employee():
    name = input("Enter employee's name: ")
    job_title = input("Enter employee's job title: ")
    department_id = input("Enter employee's department id: ")
    try:
        employee = Employee.create(name, job_title, department_id)
        print(f"Success {employee} was created")
    except Exception as exc:
        print("Error in creating employee:", exc)

def update_employee():
    id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input("Enter new employee's name: ")
            employee.name = name
            job_title = input("Enter new employee's job title: ")
            employee.job_title = job_title
            department_id = input("Enter new employee's department id: ")
            employee._department_id = department_id
            employee.update()
            print(f"Success {employee}")
        except Exception as exc:
            print("Error, new employee not created", exc)
    


def delete_employee():
    id_ = input("Enter employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f"Employee {id_} was deleted.")
    else:
        print(f"Employee {id_} was not found.")


def list_department_employees():
    pass