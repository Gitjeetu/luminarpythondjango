even=[]
odd=[]
lis=[2,5,6,8,1,7,4,3,2,1,0]
for i in lis:
    if(i%2==0):
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)