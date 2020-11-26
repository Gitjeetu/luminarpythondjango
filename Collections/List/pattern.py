lis=[1,6,5,2,3,4,4,9,10]
lis2=[]
for i in lis:
    if(i>5):
        lis2.append(i+1)
    elif(i<5):
        lis2.append(i-1)
    else:
        lis2.append(5)
print(lis2)