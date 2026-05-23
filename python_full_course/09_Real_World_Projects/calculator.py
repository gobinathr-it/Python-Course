while True:
    print("\n1.Add 2.Subtract 3.Multiply 4.Divide")
    choice = input("Choose: ")

    a = float(input("Enter A: "))
    b = float(input("Enter B: "))

    if choice == "1":
        print("Result:", a + b)
    elif choice == "2":
        print("Result:", a - b)
    elif choice == "3":
        print("Result:", a * b)
    elif choice == "4":
        print("Result:", a / b)
    else:
        print("Invalid Choice")
