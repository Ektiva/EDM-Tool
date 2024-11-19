import threading
from helpers import assign_new_ids
import read_write_employees
import schedule
import time

def periodic_task():
    employees = read_write_employees.load('employee.json')
    assign_new_ids(employees)

def start_background_scheduler():
    def run_scheduler():
        while True:
            schedule.run_pending()
            time.sleep(1)

    # Schedule the task to run every 30 seconds (adjust as needed)
    schedule.every(10).seconds.do(periodic_task)

    # Run the scheduler in a background thread
    scheduler_thread = threading.Thread(target=run_scheduler)
    scheduler_thread.daemon = True
    scheduler_thread.start()
    print("Scheduler started in the background.")