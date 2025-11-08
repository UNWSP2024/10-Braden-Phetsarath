#Braden Phetsarath
#11/5
# Program #4 Employee Class:
# Write a class Employee that holds the following data about an employee in attributes: name, ID number, department, and job title.
class Employee:
    def __init__(self, name, ID_number, department, job_title ):
        self.name = name
        self.ID_number = ID_number
        self.department = department
        self.job_title = job_title
# Once you have written the class, write a program that creates three Employee objects to hold the following data.
# Name	ID Number	Department	Job Title
# Susan Meyers	47899 	Accounting	Vice President
# Mark Jones	39119	IT	Programmer
# Joy Rogers	81774	Manufacturing	Engineer
# The program should store the data in the three objects, then display the data for each employee on the screen.
def display_employee(employee):
    print(f"Name: {employee.name}")
    print(f"ID_number: {employee.ID_number}")
    print(f"department: {employee.department}")
    print(f"job_title: {employee.job_title}")

def main():
    emp1 = Employee("Susan Meyers",	47899,	"Accounting", "Vice President")
    emp2 = Employee("Mark Jones",	39119,	"IT",	"Programmer")
    emp3 = Employee("Jor Rogers", 81774, "Manufacturing",	"Engineer")
    display_employee(emp1)
    display_employee(emp2)
    display_employee(emp3)
if __name__ == "__main__":
    main()
