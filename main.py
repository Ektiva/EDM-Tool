# from read_write_employees import {load_employee, }
from constants import DAYS_OF_WEEK, WEEKENDS
from helpers import assing_new_ids, find_employee_to_promote, find_employees_to_fire, find_max_id, group_by_favorite_day, group_employees_by_id
from prints import print_employees, print_favorite_day, print_grouped_employees
from process import run_main_menu
import read_write_employees

def main():
    employees = read_write_employees.load("employee.json")

    ## PART 1
    # print_employees(employees, "All Employees")
    # print(find_max_id(employees))cls
    # print(max(employee['name']for employee in employees)) 
    # id_groups = group_employees_by_id(employees)
    # print_grouped_employees(id_groups)
    # ordered_emp = assing_new_ids(employees)
    # print_employees(ordered_emp, "Employees with Unique Ids")

    ## PART 2
    # employee_to_promote = find_employee_to_promote(employees)
    # print_employees(employee_to_promote, "Employee To Promote:")

    ## PART 3    
    # favorite_day_groups = group_by_favorite_day(employees)
    # print(favorite_day_groups)
    # print_favorite_day(favorite_day_groups, WEEKENDS)

    ## PART 4
    # employees_to_fire, remaining_emp = find_employees_to_fire(employees)
    # print_employees(employees_to_fire, "Employees to fire: ")
    # print_employees(remaining_emp, "Remaining Employees: ")

    ## PART 5: CONSOLE APP
    run_main_menu()

    ##DRAFT
    # count = our_sum([1,2,3,4,5, 10])
    # print(count)

if __name__ == '__main__':
    main() 