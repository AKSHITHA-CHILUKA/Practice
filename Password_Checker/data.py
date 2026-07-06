class Employee:
    """Represent an employee with name, age, and salary."""
    
    def __init__(self, name, age, salary):
        """
        Initialize an employee.
        
        Args:
            name (str): Employee's name
            age (int): Employee's age
            salary (float): Employee's salary
        """
        self.name = name
        self.age = age
        self.salary = salary
    
    def __str__(self):
        """Return a string representation of the employee."""
        return f"Employee(name='{self.name}', age={self.age}, salary=${self.salary:.2f})"
    
    def __repr__(self):
        """Return a developer-friendly representation."""
        return self.__str__()
    
    def get_all_employee_info(self):
        """Return a dictionary containing all employee information."""
        return {
            "name": self.name,
            "age": self.age,
            "salary": self.salary
        }

def get_all_employee_names(employees):
    """Extract names from a list of Employee objects.
    
    Args:
        employees (list): List of Employee objects.
    
    Returns:
        list: List of employee names.
    """
    return [emp.name for emp in employees]

def get_all_employee_ages(employees):
    """Extract ages from a list of Employee objects.
    
    Args:
        employees (list): List of Employee objects.
    
    Returns:
        list: List of employee ages.
    """
    return [emp.age for emp in employees]

def get_all_employee_salaries(employees):
    """Extract salaries from a list of Employee objects.
    
    Args:
        employees (list): List of Employee objects.
    
    Returns:
        list: List of employee salaries.
    """
    return [emp.salary for emp in employees]
def get_max_salary_employee(employees):
    """Find the employee(s) with the maximum salary.
    
    Args:
        employees (list): List of Employee objects.
    
    Returns:
        list: List of Employee objects with the maximum salary.
    """
    if not employees:
        return []
    
    max_salary = max(emp.salary for emp in employees)
    return [emp for emp in employees if emp.salary == max_salary]

# Example usage
if __name__ == "__main__":
    emp1 = Employee("John Doe", 30, 50000)
    emp2 = Employee("Jane Smith", 28, 60000)
    emp3 = Employee("Alice Johnson", 35, 70000)
    emp4 = Employee("Bob Brown", 40, 80000)
    emp5 = Employee("Charlie Davis", 25, 45000)
    employees = [emp1, emp2, emp3, emp4, emp5]
    
    #print(get_all_employee_names(employees))
    #print(get_all_employee_ages(employees))
    #print(get_all_employee_salaries(employees))
    print(get_max_salary_employee(employees))
    # Output: ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob Brown', 'Charlie Davis']
