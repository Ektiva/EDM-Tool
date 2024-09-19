# from read_write_employees import {load_employee, }
from helpers import find_max_id
from prints import print_employees
import read_write_employees

def main():
    employees = read_write_employees.load("employee.json")
    # print_employees(employees)
    print(find_max_id(employees))
    # print(max(employee['name']for employee in employees)) 


if __name__ == '__main__':
    main() 