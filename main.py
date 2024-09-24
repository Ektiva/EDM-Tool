# from read_write_employees import {load_employee, }
from helpers import assing_new_ids, find_max_id, group_employees_by_id
from prints import print_employees, print_grouped_employees
import read_write_employees

def main():
    employees = read_write_employees.load("employee.json")
    # print_employees(employees, "All Employees")
    # print(find_max_id(employees))cls
    # print(max(employee['name']for employee in employees)) 
    # id_groups = group_employees_by_id(employees)
    # print_grouped_employees(id_groups)
    ordered_emp = assing_new_ids(employees)
    print_employees(ordered_emp, "Employees with Unique Ids")


if __name__ == '__main__':
    main() 