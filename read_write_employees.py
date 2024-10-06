import json

def load(file_name):
    """Load the employee data from a json file."""
    with open(file_name, 'r') as f:
        return json.load(f)