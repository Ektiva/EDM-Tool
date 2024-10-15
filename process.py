from helpers import get_employees_with_salary_range
from post_process import edm_exit, menu_callback
from prints import display_list_employee_submenu, display_main_menu, print_employees
import read_write_employees


def run_main_menu():
    display_main_menu()
    choice = input("👉 Choose a number to continue...\n").strip()

    if choice == "1":
        process_list_employee_submenu()
    elif choice == "2":
        process_update_employee_submenu()
    elif choice == "3":
        display_employee_to_reward()
    elif choice == "4":
        display_employee_to_promote()
    elif choice == "5":
        display_employee_to_fire()
    elif choice == "6":
        display_employee_working_from_home()
    elif choice == "7":
        edm_exit()

def process_list_employee_submenu():
    display_list_employee_submenu()
    employees = read_write_employees.load("employee.json")
    
    choice = input("👉 Enter your choice...\n").strip()
    if choice == "1":
        list_all_employees(employees)
    elif choice == "2":
        employees_with_salary_range(employees)
    elif choice == "3":
        employees_with_age_range()
    elif choice == "4":
        employees_by_hiring_year()
    elif choice == "5":
        employees_by_favorite_day()
    elif choice == "6":
        employee_by_name_range()
    elif choice == "7":
        run_main_menu

def process_update_employee_submenu():
    print()

def display_employee_to_reward():
    print()

def display_employee_to_promote():
    print()

def display_employee_to_fire():
    print()

def display_employee_working_from_home():
    print()

def list_all_employees(employees):
    print_employees(employees, "List of Employees")
    menu_callback(process_list_employee_submenu, run_main_menu)

def employees_with_salary_range(employees):
    emp, title = get_employees_with_salary_range(employees)
    print_employees(emp, title)

def employees_with_age_range():
    print()

def employees_by_hiring_year():
    print()

def employees_by_favorite_day():
    print()

def employee_by_name_range():
    print()

