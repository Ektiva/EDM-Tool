
from helpers import group_employees_by_id


def print_employees(employees, title):
    """Print the attributes of empoyees"""
    print("-" * 70)
    print(f"{title}: Showing {len(employees)} Result(s)")
    print("-" * 70 +"")
    headers = ["ID", "Name", "Hiring Year", "Age", "Favorite Day", "Salary"]
    row_format = "{:<5} {:<20} {:<12} {:<5} {:<15} {:<10}"
    
    print(row_format.format(*headers))
    print("-" * 70)

    if not isinstance(employees, list):
        employees = [employees] 

    # employees.sort(key=lambda emp: emp['id'])
    sorted_employees = sorted(employees, key=lambda emp: emp['id'])
    for item in sorted_employees:
        print(row_format.format(item['id'], item['name'], item['hiring_year'], item['age'], item['favorite_day'], f"${item['salary']:,}"))

def print_grouped_employees(grouped_employees):
    for emp_id, employees in grouped_employees.items():
        print_employees(employees, f"ID:{emp_id}")

def print_favorite_day(grouped_employees, days):
    for day in days:
        print_employees(grouped_employees[day], f"Working at hone on {day}")

def display_main_menu():
    """Display the main Menu of EDM tool"""
    print("╔════════════════════════════════════════════════╗")
    print("║              WELCOME TO EDM                    ║")
    print("║  Your Best Employee Data Management Tool       ║")
    print("╚════════════════════════════════════════════════╝\n")

    print("╔════════════════════════════════════════════════╗")
    print("║               🏠 MAIN MENU                     ║")
    print("║════════════════════════════════════════════════║")
    print("║  1. 📋 List Employee(s)                        ║")
    print("║  2. ✏️  Update Employee                        ║")
    print("║  3. 🎁 Employee(s) to Reward                   ║")
    print("║  4. 🎉 Employee(s) to Promote                  ║")
    print("║  5. 🔥 Employee(s) to Fire                     ║")
    print("║  6. 💻 Employee(s) Working from Home on a Day  ║ ")
    print("║  7. ↩️ Exit                                    ║")
    print("╚════════════════════════════════════════════════╝")

def display_list_employee_submenu():
    print("""
List Employee(s)
1. All Employees
2. Employee(s) within Salary Range
3. Employee(s) within Age Range
4. Employee(s) by Hiring Year
5. Employee(s) by Favorite Day
6. Employee(s) by Name Range
7. Return to Main Menu
""")

    