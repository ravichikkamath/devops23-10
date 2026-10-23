import sys

def employee_Details(name, emp_id, department, salary):
    return f"name: {name}\nEmployee ID: {emp_id}\nDepartment: {department}\nsalary: {salary}"

if __name__ == "__main__":
    name = sys.argv[1]
    emp_id = sys.argv[2]
    department = sys.argv[3]
    salary = sys.argv[4]


    print("\nEmployee Details:" )
    print("-------------------")
    print(employee_Details(name, emp_id, department, salary))
