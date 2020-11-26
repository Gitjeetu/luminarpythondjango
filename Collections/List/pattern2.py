lis=[1,1,1,1,1,1]
liz=[]
for i in lis:
    lis.remove(i)
    liz.append(sum(lis))
    lis.append(i)
print(liz)