while True:
    a = int(input("Enter the number 1 to 10 : "))

    match a:
        case 1:
            print("You won car ")
            break
        case 3:
            print("You won Bike ")
            break
        case 7:
            print("You won camera ")
            break
        case _:
            print("Better luck next time ")
