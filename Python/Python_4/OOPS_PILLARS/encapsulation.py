''' We do data hiding here
There are 3 types of  atributes:
Public - can be accessed outside and inside of class
Private - can be accessed inside the class
Protected - can be accessedd inside class + subclasses
'''

class BankAccount:
    def __init__(self , name , balance):
        self.name = name
        self.__balance = balance #data mangling
        # single underscore means protected
        # double underscore means private

        # to access private outside class we use getter function
    def get_balance(self):
        return self.__balance


        # to change private outside class we use setter function
    def set_balance(self,new_balance):
        self.__balance = new_balance
    
acc1 = BankAccount("Rahul Kumar" , 100_000)
acc1.set_balance(2000_000)
print(acc1.name , acc1.get_balance())