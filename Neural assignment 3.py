Question 1:

Input:

class Employee:
    count_of_employees = 0 

    def __init__(self, name, family, salary, department):#constructor to initialize name, family, salary, department.
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count_of_employees += 1

    def average_salary(self): #a function to average salary.
        return sum([emp.salary for emp in Employee.emps])/len(Employee.emps)

    emps = []#creating an empty list.

class FulltimeEmployee(Employee):#Creating a class and inheriting the properties from Employee class.
    pass

emp1 = Employee("snig", "tula", 50000, "Data Science")
emp2 = Employee("Sam", "Sandeep", 7000, "AI")
emp3 = FulltimeEmployee("manas", "tejaswi", 25000, "Java")
emp4 = FulltimeEmployee("Jag", "Prathi", 5000, "Aeronautics")

#Appending to 'emps' list.
Employee.emps.append(emp1)
Employee.emps.append(emp2)
Employee.emps.append(emp3)
Employee.emps.append(emp4)

print("Avg salary of the employees is: ", emp1.average_salary())
print("Number of employees: ",FulltimeEmployee.count_of_employees)

Output:

Avg salary of the employees is:  21750.0
Number of employees:  4
-----------------------------------------------------------------------------------------------
Question 2:

Input: 

import numpy as np

# Create a random vector of size 20 with float values between 1 and 20
ranvec = np.random.uniform(1, 19, 20)

# Reshape the vector to a 4x5 array
resarr = np.reshape(ranvec, (4, 5))

# Replace the maximum value in each row with 0
resarr[np.arange(resarr.shape[0]), resarr.argmax(axis=1)] = 0

print(resarr)

Output:

[[ 4.28045014  8.2568791  12.47211187  0.          5.67696128]
 [11.91720528  0.          4.87088918  2.66699847 12.59428104]
 [ 4.5315723   9.69233191  4.74485734  1.00647219  0.        ]
 [12.80739783 10.65881794  1.85776185 15.14330126  0.        ]]