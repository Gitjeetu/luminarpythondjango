f=open("details.py","r")
emp={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    for word in words:
        id=word[0]
        name=word[1]
        desig=word[2]
        exp=word[3]
        sal=word[4]
        emp[id]={"id":id,"name":name,"desig":desig,"exp":exp,"sal":sal}

def printemployee(**kwargs):
    if id in kwargs:
        print(emp)