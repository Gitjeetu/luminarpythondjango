f=open("movies.csv","r")
di={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    year=words[2]
    if year not in di:
        di[year]=1
    elif year in di:
        di[year]+=1
print(di)
print(di["1992"])
high=max(di,key=di.get)
print(high,di[high])