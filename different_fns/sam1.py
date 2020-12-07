def add(*n):
    sum=0
    for i in n:
        sum+=i
    return(sum)
a=add(1,2,3,3,4)
print(a)

def print_data(**kwargs):
    for k,v in kwargs.items():
        print(k,v)

print_data(dob="22/10/98",nation="India",work="America")