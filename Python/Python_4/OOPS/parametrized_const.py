# Have multtiple parameters other than self

class Student():
    def __init__(self,name,cgpa): #self is a mandatory parameter which means the current object.
        self.name = name
        self.cgpa = cgpa

    def get_cgpa(self):
        return self.cgpa

    
stu1 = Student("Rahul",9.0)
stu2 = Student("Ayush",9.6)
stu3 = Student("Joiya",8.3)

print(stu1.cgpa)
print(stu2.name)
print(stu3.name)

print(f"{stu1.name} has cgpa = {stu1.get_cgpa()}")