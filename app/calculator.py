from app.operaciones import sum, subtract, multiply, divide

def calculator():
    """ """
    print("1 Sum")
    print("2 Subtract")
    print("3 Multiply")
    print("4 Divide")
    
    option=input("choose the operation: ")
    
    num1 = float(input("Put the first number: "))
    num2 = float(input("Put the second number: "))
    
    if option == "1":
        print("Result: ",sum(num1,num2))
    elif option == "2":
        print("Result: ",subtract(num1,num2))
    elif option == "3":
        print("Result: ",multiply(num1,num2))
    elif option == "4":
        print("Result: ",divide(num1,num2))

if __name__ == "__main__":
    calculator()