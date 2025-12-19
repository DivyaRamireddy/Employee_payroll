# employee_payroll.py
# OOP-based Employee Payroll System

class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def calculate_salary(self):
        pass


class FullTimeEmployee(Employee):
    def __init__(self, emp_id, name, monthly_salary):
        super().__init__(emp_id, name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, emp_id, name, hours_worked, rate_per_hour):
        super().__init__(emp_id, name)
        self.hours_worked = hours_worked
        self.rate_per_hour = rate_per_hour

    def calculate_salary(self):
        return self.hours_worked * self.rate_per_hour


if __name__ == "__main__":
    emp1 = FullTimeEmployee(101, "Divya", 40000)
    emp2 = PartTimeEmployee(102, "Reddy", 80, 300)

    print("Employee Payroll Details")
    print("------------------------")
    print(f"{emp1.name} Salary: ₹{emp1.calculate_salary()}")
    print(f"{emp2.name} Salary: ₹{emp2.calculate_salary()}")
