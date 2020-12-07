f=open("covid_19_india.csv","r")
di={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    state=words[3].rstrip("***")
    conf=int(words[8])
    if(state not in di):
        di[state]=conf
    else:
        di[state]=conf
high=max(di,key=di.get)
print(high)
lst=[]
for k,v in di.items():
    lst.append([v,k])
lst=sorted(lst,reverse=True)
print(lst)
