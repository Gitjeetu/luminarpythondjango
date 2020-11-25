name=input("Enter your name")
age=int(input("Enter your age"))
if (age<18):
    print(name,"is ineligible for voting coz under age",age)
elif (age>18):
    print(name, "is eligible for voting with age", age)