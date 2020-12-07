st="hi how are you hi how are you"
lis=st.split(" ")
dic1={}
for word in lis:
    if word not in dic1:
        dic1[word]=1
    else:
        dic1[word]+=1
print(dic1)