class Employee:
    start_time = "10am"
    end_time = "6pm"

    def change_time(self,new_end_time):
        self.end_time = new_end_time

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject

class AdminStaff(Employee):
    def __init__(self,role):
            self.role = role



t1 = Teacher("math")
t1.change_time("2pm")
print(t1.subject , t1.start_time,t1.end_time)


s1 = AdminStaff("manager")
print(s1.role, s1.start_time,s1.end_time)