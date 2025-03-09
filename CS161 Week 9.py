# Adam Fitzpatrick
# Week 9

#1
class Students:
    """Sets a class for students and initializes the attributes
        name, age and grade. The passes the Self argument to the full_details method"""
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade

    def student_details(self):
        """ Method to print the details passed from students in a formated fashion"""
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Grade: {self.grade}")
        print()

# Passes information for each student to the class students
student_one = Students("Adam", 35,"3rd")
student_two = Students("James", 4,"Preschool")

# calls the class function
student_one.student_details()
student_two.student_details()

#2
class Staff:
    """Sets a class for staff, initializes the attributes name, department, and role."""
    def __init__(self, name, department, role):
        self.name = name
        self.department = department
        self.role = role

class Teacher(Staff):
    """Sets a class for teacher, inherits the attributes name, department, and role
        from the parent class(Staff) and initializes an additional attribute age.  """
    def __init__(self, name, age, department, role):
        super().__init__(name, department, role)
        self.age = int(age)

    def staff_information(self):
        """ Method to print the staff information in a formated fashion"""
        print(f"Name: {self.name}\n"
              f"Age: {self.age}\n"
              f"Department: {self.department}\n"
              f"Role: {self.role}"
              )
        print()
# passes information for each staff member to the class Teacher
staff_one = Teacher("James", 29,"P.E", "Teacher")
staff_two = Teacher("Adam",32, "Math", "Failure")

# calls the class function
staff_one.staff_information()
staff_two.staff_information()

#3
class Squares:
    """ Defines a class Square that initializes a single attribute x"""
    def __init__(self, x):
        self.x = x

    def area(self):
        """ Method to multiply the attribute x by itself to find the area """
        return self.x * self.x

    def perimeter(self):
        """ Method to multiply the attribute x by 4 to find the perimeter """
        return self.x * 4
# Calls the class function Squares with the values for x
square_one = Squares(10)
square_two = Squares(7)

# Prints the information passed through the functions.
print(f"The area of the first square is: {square_one.area()}\n"
      f"The Perimeter of first square is: {square_one.perimeter()}\n")
print(f"The area of the first square is: {square_two.area()}\n"
      f"The Perimeter of first square is: {square_two.perimeter()}\n")