from collections import defaultdict

from constants import DAYS_OF_WEEK, WEEKDAYS
import read_write_employees


def find_max_id(employees):
    max_id = 0
    for employee in employees:
        if employee['id'] > max_id:
            max_id = employee['id']
    return max_id

def group_employees_by_id(employees):
    """Group employees by id"""
    # id_groups = {}
    # for emp in employees:
    #     emp_id = emp['id']
    #     if emp_id not in id_groups:
    #         # id_groups[emp_id] = []  
    #         id_groups[emp_id].append(emp)       
    #     else:
    #         id_groups[emp_id].append(emp)

    ## Using defaultDictionary
    id_groups = defaultdict(list)
    for emp in employees:
        id_groups[emp['id']].append(emp)  

    return id_groups

def assing_new_ids(employees):
    new_employees = []
    max_id = find_max_id(employees)
    id_groups = group_employees_by_id(employees)

    # Resolve duplicates
    for emp_list in id_groups.values():
        if len(emp_list) > 1:
            emp_list.sort(key=lambda emp: (emp['hiring_year'], -emp['age']))
            for index, emp in enumerate(emp_list):
                if index > 0:
                    emp['id'] = max_id + 1
                    new_employees.append(emp)
                    max_id = max_id + 1
                else:
                    new_employees.append(emp)
        else:
            new_employees.append(emp_list[0])
    return new_employees

def find_employee_to_promote(employees):
    emp_to_promote = employees[0]

    for emp in employees:
        if emp['age'] > emp_to_promote['age']:
            emp_to_promote = emp
        elif emp['age'] == emp_to_promote['age']:
            if emp['hiring_year'] < emp_to_promote['hiring_year']:
                emp_to_promote = emp
    return emp_to_promote

def group_by_favorite_day(employees):
    favorite_day_groups = defaultdict(list)
    for emp in employees:
        day = emp['favorite_day']
        if day in DAYS_OF_WEEK:
            favorite_day_groups[day].append(emp)
            
    return favorite_day_groups

def find_employees_to_fire(employees):
    fired_emp = []
    remaining_emp = []

    for emp in employees:
        if emp['age'] < 30 and emp['favorite_day'] in WEEKDAYS and 2024 - emp['hiring_year'] < 2 and emp['salary'] > 50000:
            fired_emp.append(emp)
        else:
           remaining_emp.append(emp) 

    return remaining_emp, fired_emp

find_employees_to_fire(read_write_employees.load("employee.json"))

def get_employees_with_salary_range(employees):
    min_salary_input = input("Enter minimum salary (leave blank if not applicable): ").strip()
    max_salary_input = input("Enter maximum salary (leave blank if not applicable): ").strip()

    min_salary = None
    max_salary = None

    if min_salary_input:
        min_salary = int(min_salary_input)
    if max_salary_input:
        max_salary = int(max_salary_input)

    filtered_employees = []
    for emp in employees:
        value = emp['salary']
        if (min_salary is None or value >= min_salary) and (max_salary is None or value <= max_salary):
            filtered_employees.append(emp)
    
    title = "" 
    if min_salary is not None and max_salary is not None:
        title = f"Employee(s) within salary range {min_salary} to {max_salary}" 
    elif min_salary is not None:
        title =f"Employee(s) with salary above {min_salary}"
    elif max_salary is not None:
        title =f"Employee(s) with salary below {max_salary}"
    else :
        title = "All Employees"

    return filtered_employees, title
