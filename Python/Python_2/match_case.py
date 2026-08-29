color = input("enter color: ")
match color:
    case "Green":
        print("Go")
    case "Red":
        print("Stop")
    case "Yellow":
        print("Ready")
    case _:
        print("Wrong color")