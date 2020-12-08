f=open("covid_19_india.csv","r")
covid={}
for lines in f:
    sl,date,time,state,athome,athosp,totalcases,death,active=lines.rstrip("\n").split(",")
    if state not in covid:
        covid[state]={"sl":sl,"date":date,"time":time,"athome":athome,"athosp":athosp,"death":death,"active":active}
    else:
        covid[state]={"sl":sl,"date":date,"time":time,"athome":athome,"athosp":athosp,"death":death,"active":active}
print(covid)

def print_state(**kwargs):
    st=kwargs["state"]
    if st in covid:
        print(covid[st]["state"])
        if "death" in kwargs:
            prop="death"
            if prop in covid[st]:
                print(students[st][prop])
            else:
                print("invalid property")
    else:
        print("student doesnt exist")

print_state(state="Kerala")