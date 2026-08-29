name = input("Enter Username: ")
password = int(input("Enter Password: "))
if(name  == "admin" and password == 123):
    print("Access Granted")
elif(name != "admin"):
    print("Wrong username")
else:
    print("Wrong Password")
    