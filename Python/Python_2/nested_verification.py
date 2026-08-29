name = input("Enter Username: ")
password = int(input("Enter Password: "))
if(name  == "admin" and password == 123):
    print("Access Granted")
else:
    if(name != "admin"):
        print("Wrong username")
    else:
        print("wrong pasword")
