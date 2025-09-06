
#HW 01 CS 605 class (Cal. app)

print("Hello there, ready to use the calculator?")
while True:
    while True:
        try:
            first_numb = float(input("enter the first number: "))
            break
        except ValueError:
            print("Please enter a number, try again ")
    
    while True:
        try:
            second_numb = float(input("enter the second number: "))
            break
        except ValueError:
            print("Please enter a number, try again ")

    print("Available operations to choose from")
    print("1. Additon")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        numbers_to_perform = input("Select one of the number of operations to do: ")
        if numbers_to_perform == "1":
            operation = first_numb + second_numb
            break
        elif numbers_to_perform == "2":
            operation = first_numb - second_numb
            break
        elif numbers_to_perform == "3":
            operation = first_numb * second_numb
            break
        elif numbers_to_perform == "4":
            if second_numb != 0:
                operation = first_numb / second_numb
            else:
                operation = "Operation not allowed, Div. by zero"
            break
        else:
            print("Try again and select one of the number options to perform")

    print("Result:", operation)
    
    # Ask if user wants to do another calculation
    repeat = input("\nDo you want to do another calculation? type 'yes' to continue or any key to exit: ").lower()
    if repeat != "yes":
        print("Thank you. Goodbye!")
        break