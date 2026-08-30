# An attribute is a variable/data that belongs to an object.
# There are 2 types of attributes:
# Class - Belong to class
# instance - belong to object

class Student:
    college_name = "ABC college"  #class
    def __init__(self,name,gpa):
        self.name = name #instance
        self.gpa = gpa  

stu1 = Student("Rahul" , 9.2)
print(Student.college_name)

