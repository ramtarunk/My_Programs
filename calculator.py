def Addition(num1,num2):
    x = lambda a, b : b + a
    print("Addition of entered 2 numbers is : ", x(num1,num2))
    return 0

def Subtraction(num1,num2):
    x = lambda a, b: a-b
    print("Subtraction of entered 2 numbers is :", x(num1,num2))
    return 0
def Multiplication(num1,num2):
    x = lambda a, b: b * a
    print("Multiplication of entered 2 numbers is : ", x(num1,num2))
    return 0
def Division(num1,num2):
    x = lambda a, b: a/b
    print("Division of 2 numbers is : ", x(num1,num2))
    return 0

i=1
while i < 2:
    num1 = int(input("Enter the number 1: "))
    num2 = int(input("Enter the number 2: "))
    print("Enter the option to perform: \n1. Addtion \n2. Subtraction \n3. Multiplication \n4. Division \n5.Repeat the same operation \n")
    option = int(input("Enter the option to perform : "))

    if option == 1:
        Addition(num1,num2)

    elif option == 2:
        Subtraction(num1,num2)
    elif option == 3:
        Multiplication(num1,num2)
    elif option == 4:
        Division(num1,num2)

    else:
        print("You entered the wrong value")
        print("Do you want to Repeat the same operation")
        a = str(input("Enter your option either Y, N"))
        if a == 'Y' or a == 'y':
            continue
        else:
            i=2
            exit()



