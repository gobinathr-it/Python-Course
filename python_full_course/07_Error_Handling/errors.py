try:
    num = int(input("Enter number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Zero division error")
except ValueError:
    print("Invalid input")
