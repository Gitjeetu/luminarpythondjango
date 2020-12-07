f1=open("names.txt","r")
f2=open("passed.txt","r")
def converted(file):
    fset=set()
    for lines in file:
        fset.add(lines.rstrip("\n"))
    return(fset)

namset=converted(f1)
paset=converted(f2)
res=namset-paset
print(res)