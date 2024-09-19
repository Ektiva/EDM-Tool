
def print_employees(employees):
    """Print the attributes of empoyees"""

    headers = ["ID", "Name", "Hiring Year", "Age", "Favorite Day", "Salary"]
    row_format = "{:<5} {:<20} {:<12} {:<5} {:<15} {:<10}"
    
    print(row_format.format(*headers))
    print("-" * 70)
    
    for item in employees:
        print(row_format.format(item['id'], item['name'], item['hiring_year'], item['age'], item['favorite_day'], f"${item['salary']:,}"))

