lst=[1,4,2,8,5,9,3]
lst.sort()
print(lst)
low=0
upper=len(lst)-1
fl=0
el=int(input("Enter element to be searched for:"))
while(low<=upper):
    mid=(low+upper)//2 #mid=int((low+upper)/2)
    if(el>lst[mid]):
        low=mid+1
    elif(lst[mid]>el):
        upper=mid-1
    elif(el==lst[mid]):
        fl=1
        break
if(fl==1):
    print("Element found")
else:
    print("element not found")