st="ababac"
lis=[]
for i in st:
    if i not in lis:
        lis.append(i)
    else:
        print(i)
        break
print(lis)