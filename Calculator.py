# Calculator Application by Dylan Duru: Last Updated 3/31/2020

cont = "Y"


def validNum(n) :  # Checks to make sure the user inputs a number
    try :
        float(n)
        return True
    except ValueError :
        return False


def validChoice(c) :  # Checks to make sure the user inputs an operator
    if c == '+' or c == '-' or c == '*' or c == '/' or c == 'x' :
        return True
    else :
        return False


def power(bnum, pnum) :  # Exponent
    product = 1
    for index in range(int(pnum)) :
        product = product * int(bnum)
    return product


while cont == 'Y' or cont == 'y' :  # Loops calculator operations
    valid = False  # Checks for invalid statements
    while not valid :
        num1 = input("Enter 1st number: ")
        choice = input("Are you Adding(+), Subtracting(-), Multiplying(*), Dividing(/), or using an Exponent(x)?: ")
        num2 = input("Enter 2nd number: ")
        if validNum(num1) and validNum(num2) and validChoice(choice) :
            valid = True
        else :
            print("Invalid argument. Please try again")

    if choice == '+' :
        oper = "addition"
        result = float(num1) + float(num2)
    elif choice == '-' :
        oper = "subtraction"
        result = float(num1) - float(num2)
    elif choice == '*' :
        oper = "multiplication"
        result = float(num1) * float(num2)
    elif choice == '/' :
        oper = "division"
        result = float(num1) / float(num2)
    elif choice == 'x' :
        oper = "equation's"
        result = float(power(num1, num2))

    print("The " + oper + ' result is: ' + str(result))
    cont = input("Continue?(Y/N): ")
print("Goodbye.")
