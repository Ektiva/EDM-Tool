def find_max_id(employees):
    max_id = 0
    for employee in employees:
        if employee['id'] > max_id:
            max_id = employee['id']
    return max_id
        