l=int(input("Enter lower limit"))
h=int(input("Enter higher limit"))
evsum=0
odsum=0
while l<=h:
    if l%2==0:
        evsum=evsum+l
    elif l%2!=0:
        odsum=odsum+l
    l+=1
print("Evensum:",evsum)
print("oddsum:",odsum)