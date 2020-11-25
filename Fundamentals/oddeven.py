print("Enter three distinct numbers please!!!")
num1=int(input("Enter a number1:"))
num2=int(input("Enter a number2:"))
num3=int(input("Enter a number3:"))
if num1>num2>num3:
    sor1=num1
    sor2=num2
    sor3=num3
elif num1>num3>num2:
    sor1=num1
    sor2=num3
    sor3=num2
elif num2>num1>num3:
    sor1=num2
    sor2=num1
    sor3=num3
elif num2>num3>num1:
    sor1=num2
    sor2=num3
    sor3=num1
elif num3>num2>num1:
    sor1=num3
    sor2=num2
    sor3=num1
elif num3>num1>num2:
    sor1=num3
    sor2=num1
    sor3=num2
else:
    print("Error!!\n")
    print("Same number Entered more than Once!!!")
    if num1==num2:
        if num1>num3:
            print("Second largest:",num3)
        else:
            print("Second largest:",num1)
    elif num1==num3:
        if num1>num2:
            print("Second largest:",num2)
        else:
            print("Second largest:",num1)
    elif num2==num3:
        if num2>num1:
            print("Second largest:",num1)
        else:
            print("Second largest:",num2)
    if num1==num2==num3:
        print("All numbers are same!!!!")

    exit()

print("Sorted Order:",sor1,sor2,sor3)
print("Second largest Number:",sor2)

