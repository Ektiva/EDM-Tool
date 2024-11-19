import json

def load(file_name):
    """Load the employee data from a json file."""
    with open(file_name, 'r') as f:
        return json.load(f)
    
def update(employees, file_name):
    """Save the employee data to a json file."""
    with open(file_name, 'w') as f:
        return json.dump(employees, f, indent=4)
    
    