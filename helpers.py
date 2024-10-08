from collections import defaultdict
from read_write_employees import load

from constants import DAYS_OF_WEEK, WEEKENDS
from constants import WEEKDAYS
import read_write_employees
from datetime import datetime


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

def employees_reward_count(employees):
    grouped_employees_to_rewards = group_by_favorite_day(employees)
    count = 0
    for day in WEEKENDS:
        number = len(grouped_employees_to_rewards[day])
        count += number
    return count

def find_employees_to_reward(employees):
    grouped_employees_to_rewards = group_by_favorite_day(employees)
    employees_name = []
    for day in WEEKENDS:
        employees_name.extend(grouped_employees_to_rewards[day])
    return employees_name

# find_employees_to_reward(load('employee.json'))

# def find_employee_to_fire(employees):
#     emp_to_fire = defaultdict(list)
#     day = emp['favorite_day']
#     current_year = int(datetime.now().year)
#     year_of_service = current_year - int(datetime.now().year)

#     for emp in employees:
#         if emp['age'] < 30 and year_of_service < 2:
#            emp_to_fire['age'].append(emp)
#            print(emp_to_fire)


#         # elif emp['age'] == emp_to_fire['age']:
#         #     if emp['hiring_year'] < emp_to_promote['hiring_year']:
#         #         emp_to_promote = emp
#     # return emp_to_fire