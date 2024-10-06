from datetime import datetime

def calculate_age(year_of_birth):
    """Calculate age based on the year of birth."""
    current_year = datetime.now().year
    return current_year - year_of_birth

print(calculate_age(1994))