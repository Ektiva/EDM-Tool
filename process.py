from helpers import add_employee, edit_employee, find_employee_to_promote, find_employees_to_fire, get_employees_by_name_initial, get_employees_with_age_range, get_employees_with_attribute_range, get_employees_with_salary_range, get_employees_with_specific_attribute, remove_employee
from post_process import edm_exit, menu_callback
from prints import display_list_employee_submenu, display_main_menu, display_update_employee_submenu, print_employees
import read_write_employees


def run_main_menu():
    display_main_menu()
    choice = input("👉 Choose a number to continue...\n").strip()
    employees = read_write_employees.load("employee.json")

    if choice == "1":
        process_list_employee_submenu(employees)
    elif choice == "2":
        process_update_employee_submenu(employees)
    elif choice == "3":
        display_employee_to_reward(employees)
    elif choice == "4":
        display_employee_to_promote(employees)
    elif choice == "5":
        display_employee_to_fire(employees)
    elif choice == "6":
        display_employee_working_from_home(employees)
    elif choice == "7":
        edm_exit()

def process_list_employee_submenu(employees):
    display_list_employee_submenu()
    
    choice = input("👉 Enter your choice...\n").strip()
    if choice == "1":
        list_all_employees(employees)
    elif choice == "2":
        employees_with_salary_range(employees)
    elif choice == "3":
        employees_with_age_range(employees)
    elif choice == "4":
        specific_employees(employees, "hiring_year")
    elif choice == "5":
        specific_employees(employees, "favorite_day")
    elif choice == "6":
        employee_by_name_range(employees)
    elif choice == "7":
        return run_main_menu

def process_update_employee_submenu(employees):
    display_update_employee_submenu()
    choice = input("👉 Enter your choice...\n").strip()

    if choice == "1":
        update_employees(employees, "Add")
    elif choice == "2":
        update_employees(employees, "Remove")
    elif choice == "3":
        update_employees(employees, "Edit")
    elif choice == "4":
        return run_main_menu()
    else:
        print("\n Invalid choice. Please try again.")
        return process_update_employee_submenu()
    
def display_employee_to_reward(employees):
    print()

def display_employee_to_promote(employees):
    employee_to_promote = find_employee_to_promote(employees)
    print_employees(employee_to_promote, "List of Employees to promote")
    menu_callback(process_list_employee_submenu, run_main_menu)

def display_employee_to_fire(employees):
    remaining_emp, employee_to_fire = find_employees_to_fire(employees)
    print_employees(employee_to_fire, "List of Employees to Fire")
    menu_callback(process_list_employee_submenu, run_main_menu)

def display_employee_working_from_home(employees):
    print()

def list_all_employees(employees):
    print_employees(employees, "List of Employees")
    menu_callback(process_list_employee_submenu, run_main_menu)

def employees_with_salary_range(employees):
    emp, title = get_employees_with_attribute_range(employees, "salary")
    print_employees(emp, title)
    menu_callback(process_list_employee_submenu, run_main_menu)

def employees_with_age_range(employees):
    emp, title = get_employees_with_attribute_range(employees, "age")
    print_employees(emp, title)
    menu_callback(process_list_employee_submenu, run_main_menu)

def employees_by_hiring_year():
    print()

def employees_by_favorite_day():
    print()

def specific_employees(employees, attribute):
    emp, title = get_employees_with_specific_attribute(employees, attribute)
    print_employees(emp, title)
    menu_callback(process_list_employee_submenu, run_main_menu)

def employee_by_name_range(employees):
    emp, title = get_employees_by_name_initial(employees)
    print_employees(emp, title)
    menu_callback(process_list_employee_submenu, run_main_menu)

def update_employees(employees, action):
    emp = {}

    if (action == "Add"):
        emp = add_employee(employees)
    elif(action == "Remove"):
        emp = remove_employee(employees)
    elif(action == "Edit"):
        emp = edit_employee(employees)
    
    print_employees(emp, "Updated List of Employees")
    
    menu_callback(process_update_employee_submenu, run_main_menu)

