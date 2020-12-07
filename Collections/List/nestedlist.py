lst_a=[[110,"Arjun","mba",160],[118,"Indu","mca",165],[121,"Thangs","mca",170],[121,"jangs","bcom",170]]
tot=0
for student in lst_a:
    tot=tot+student[3]
print(tot)
mca=0
mba=0
bcom=0
for student in lst_a:
    if(student[2]=="mca"):
        mca+=1
    elif (student[2] == "mba"):
        mba+=1
    elif(student[2]=="bcom"):
        bcom+=1
print("mca:",mca)
print("mba:",mba)
print("bcom",bcom)
print(max(mba,mca,bcom))
