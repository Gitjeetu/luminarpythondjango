lst=[1,5,2,8,3,4,6,7]
a=int(input("Enter your number"))
sum=0
for i in lst:
    for j in lst:
        if(i==j):
            continue
        elif(i+j==a):
            print(i,j)
            break
    break