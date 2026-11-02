class Employee:
    def __init__(self, employee_id, employee_name, department, leave_balance):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.leave_balance = leave_balance
    def apply_leave(self, days):
        if days <= 0:
            print("Invalid Leave Request")
        elif days <= self.leave_balance:
            self.leave_balance -= days
            print("Leave Approved")
        else:
            print("Insufficient Leave Balance")
    def cancel_leave(self, days):
        if days <= 0:
            print("Invalid Cancellation")
        else:
            self.leave_balance += days
    def check_balance(self):
        print("Leave Balance:", self.leave_balance)
    def display_employee(self):
        print("Employee ID:", self.employee_id)
        print("Employee Name:", self.employee_name)
        print("Department:", self.department)
        print("Leave Balance:", self.leave_balance)
data = input().split()
if len(data) != 4:
    print("Invalid employee details")
    exit()
employee_id = data[0]
employee_name = data[1]
department = data[2]
leave_balance = int(data[3])
emp = Employee(employee_id, employee_name, department, leave_balance)
n = int(input())
for i in range(n):
    operation = input().split()
    if operation[0] == "APPLY":
        days = int(operation[1])
        emp.apply_leave(days)
    elif operation[0] == "CANCEL":
        days = int(operation[1])
        emp.cancel_leave(days)
    elif operation[0] == "BALANCE":
        emp.check_balance()
    elif operation[0] == "DISPLAY":
        emp.display_employee()
