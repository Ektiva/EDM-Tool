from collections import defaultdict

from constants import DAYS_OF_WEEK
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