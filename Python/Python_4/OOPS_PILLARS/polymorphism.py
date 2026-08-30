# Function Overriding - Function overriding means when a child class provides its own version of a method that already exists in the parent class.
class Employee:
    def get_designation(self):
        print("designation = Employee")


class Teacher(Employee):
    def get_designation(self):
        print("designation = Teacher")


t1 = Teacher()
t1.get_designation()


# Duck Typing : 
# Duck typing means Python cares about what an object can do, rather than what type/class it is.
# "If it walks like a duck and quacks like a duck, treat it like a duck."

class Teacher:
    def get_designation(self):
        print("designation = Teacher")


class Accountant:
    def get_designation(self):
        print("designation = Accountant")


t1 = Teacher()
t1.get_designation()

acc1 = Accountant()
acc1.get_designation()