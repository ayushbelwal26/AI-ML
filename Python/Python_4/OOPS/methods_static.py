'''
1. No compulsory parameter 
2. They can't access neither instance nor class
3. Uses decorator: @staticmethod
'''

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


    @staticmethod
    def calc_disc(price,discount):
        final_price = price - (discount*price/100)
        print(f"discounted price = {final_price}")

l1= Laptop("16gb","512gb")
l2 = Laptop("8gb" , "256gb")

l1.get_info()
Laptop.get_storage()
l1.get_storage()

l1.calc_disc(40_000,10)
