def print_student(**kwargs):
    rol=kwargs["id"]
    if rol in students:
        print(students[rol]["name"])
        if "property" in kwargs:
            prop=kargs["property"]
            if prop in students[rol]:
                print(students[rol][prop])
        else:
            print("invalid property")
    else:
        print("student doesnt exist")

