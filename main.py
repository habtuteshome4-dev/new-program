balance=100
while True:
    print("1.Check balance.")
    print("2.Send money.")
    print("3.Buy airtime.")
    print("4.Deposite.")
    print("5.EXIT.")

    option=input("Enter your option: ")
    if option=="1":
        print (f"Your current balance is",balance,"ETB.")
        break
    elif option =="2":
        account=input("Enter your account: ")
        if account=="123456789":
            amount=int(input("Enter the amount: "))
            if amount <= balance:
                balance=balance-amount
                print(f"Succsful,Your current balance ",balance,"ETB.")
            else:
                print("Your balance is insuficient.")
        else:
            print("Invalied account number.")
        break
    elif option=="3":
        phone=input("Enter phone number: ")
        if phone =="0912345678":
            amount=int(input("Enter amount: "))
            if amount <= balance:
                balance=balance-amount
                print(f"Succsful, Your current balance", balance,"ETB.")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid phone number.")
        break
    elif option=="4":
        deposite=int(input("Enter amount: "))
        balance=balance+deposite
        print("Your current balance", balance,"ETB")
        break
    elif option=="5":
        print("Good bay.")
        break
    else:
        print("Invalied option.")
        break