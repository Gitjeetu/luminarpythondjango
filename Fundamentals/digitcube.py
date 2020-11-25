x=int(input("Enter your number:"))
csum=0
while x>0:
    digit=x%10
    csum=csum+digit**3
    x=x//10
print("Sum of cubes of all digits is:",csum)