n=int(input("Enter your number:"))
nmin=int(input("Enter lower limit:"))
nmax=int(input("Enter upper limit:"))
for i in range(nmin,nmax+1):
    if(i**n<=nmax) and (i**n>=nmin):
        print(i,":",i,"^",n,"=",i**n)