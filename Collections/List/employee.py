employees=[[1001,"ajay","qa",1981,1987],[1002,"vijay","developer",1990,2000]]
for employee in employees:
    print(employee[2])
for employee in employees:
    if (employee[3]>=1980):
        if employee[4]<1990:
            print("*")
            print(employee)
for employee in employees:
    if employee[4]-employee[3]>9:
        print(employee)