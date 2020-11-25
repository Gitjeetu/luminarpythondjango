l=int(input("Enter low:"))
h=int(input("Enter high:"))
print("limit is from",l,"to",h)
for num in range(l,h+1):
    fl=0
    for i in range(2,num):
        if(num%i==0):
            fl+=1
    if(fl==0):
        print(num)