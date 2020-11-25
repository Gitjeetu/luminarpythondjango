
l=int(input("Enter your lower limit"))
h=int(input("Enter your higher limit"))


for num in range(l,h+1):
    fl=0
    for i in range(2,num):
        if(num%i==0):
            fl+=1
        if fl==0:
            print(i)
        else:
            continue
