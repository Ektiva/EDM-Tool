
from helpers import group_employees_by_id


def print_employees(employees, title):
    """Print the attributes of empoyees"""
    print("-" * 70)
    print(f"{title}")
    print("-" * 70)
    headers = ["ID", "Name", "Hiring Year", "Age", "Favorite Day", "Salary"]
    row_format = "{:<5} {:<20} {:<12} {:<5} {:<15} {:<10}"
    
    print(row_format.format(*headers))
    print("-" * 70)
    
    for item in employees:
        print(row_format.format(item['id'], item['name'], item['hiring_year'], item['age'], item['favorite_day'], f"${item['salary']:,}"))

def print_grouped_employees(grouped_employees):
    for emp_id, employees in grouped_employees.items():
        print_employees(employees, f"ID:{emp_id}")
    