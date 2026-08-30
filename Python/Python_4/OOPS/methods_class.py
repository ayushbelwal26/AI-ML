# 1st parameter is cls
# can only access class attribute
# We use decorator @classmethod -> changes behaviour
# @classmethod is a decorator used to create a method that belongs to the class, rather than a particular object.

# A class method receives cls as its first parameter instead of self.

class Laptop:
    storage_type = "ssd"

    def __init__(self,RAM,storage):
        self.RAM = RAM
        self.storage = storage

    @classmethod
    def get_storage(cls):
        print(f"storage type = {cls.storage_type}")


    def get_info(self):
        print(f"laptop has {self.RAM} RAM & {self.storage} {self.storage_type}")


l1= Laptop("16gb","512gb")
l2 = Laptop("8gb" , "256gb")

l1.get_info()
Laptop.get_storage()
l1.get_storage()
