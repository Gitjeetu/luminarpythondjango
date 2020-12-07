f=open("dataa.py","r")
lst=[]
for lines in f:
    words=lines.rstrip(".\n")
    for word in words:
        lst.append(word)
print(lst)