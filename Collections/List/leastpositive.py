lis=[-3,-2,-1,0,1,2,3,4]
num=0
for i in range(0,len(lis)-1):
    if(lis[i]<0):
        pass
    elif(lis[i+1]-lis[i]!=1):
        num=(lis[i]+1)
        break
    else:
        num=(lis[len(lis)-1]+1)
        break
print(num)
