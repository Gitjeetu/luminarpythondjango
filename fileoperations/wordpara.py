f=open("dataa.py","r")
di={}
for lines in f:
    words=lines.rstrip(".\n").split(" ")
    for word in words:
        if(word not in di):
            di[word]=1
        else:
            di[word]+=1
print(di)
fl=0
for k in di:
    if(di[k]>fl):
        fl=di[k]
print("max",max(di))
print("The maximum word counts are for word(s):")
print("---------------")
print("word/count")
print("---------------")
for k in di:
    if(di[k]==fl):
        print(k,"/",fl)