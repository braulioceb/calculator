from calculator.app.operaciones import sum, subtract, multiply, divide, root

def calculator():
    """ """
    print("1 Sum")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    print("6 Divide")
    
    option=input("choose the operation: ")
    
    num1 = float(input("Put the first number: "))
    num2 = float(input("Put the second number: "))
    
    if option == "1":
        print("Result: ",sum(num1,num2))
        return sum(num1,num2)
    elif option == "2":
        print("Result: ",subtract(num1,num2))
        return subtract(num1,num2)
    elif option == "3":
        print("Result: ",multiply(num1,num2))
        return multiply(num1,num2)
    elif option == "4":
        print("Result: ",divide(num1,num2))
        return divide(num1,num2)
    elif option == "6":
        print("Result: ", root(num1,num2))
        return root(num1,num2)

if __name__ == "__main__":
    calculator()