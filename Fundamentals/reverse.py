n=int(input("Enter number:"))
rev=0
while n>0:
    x=n%10
    rev=rev*10+x
    n=n//10
print("Reverse:",rev)

