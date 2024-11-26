import json, os

def get_path(file_name):
    # Get the directory where the executable/script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))
    # Construct the full path to the JSON file
    return os.path.join(base_dir, file_name)

def update(employees, file_name):
    """Save the employee data to a json file."""
    file_path = get_path(file_name)
    with open(file_path, 'w') as f:
        return json.dump(employees, f, indent=4)
    
def load(file_name):
    """Load the employee data from a JSON file."""
    file_path = get_path(file_name)
    with open(file_path, 'r') as f:
        return json.load(f)