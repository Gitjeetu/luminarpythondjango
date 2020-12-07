f1=open("students.txt","r")
students={}
for lines in f1:
    rol,name,course,total=lines.rstrip("\n").split(",")
    if rol not in students:
        students[rol]={"rol":rol,"name":name,"course":course,"total":total}
    else:
        pass

print(students)


def print_student(**kwargs):
    rol=kwargs["id"]
    if rol in students:
        print(students[rol]["name"])
        if "property" in kwargs:
            prop=kwargs["property"]
            if prop in students[rol]:
                print(students[rol][prop])
            else:
                print("invalid property")
    else:
        print("student doesnt exist")

print_student(id="101",property="total")