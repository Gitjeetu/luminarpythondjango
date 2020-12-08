f=open("covid_19_india.csv","r")
covid={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    state=data[3]

    if state not in covid:
        covid[state]={"sl":sl,"date":date,"time":time,"athome":athome,"athosp":athosp,"death":death,"active":active}
    else:
        covid[state]={"sl":sl,"date":date,"time":time,"athome":athome,"athosp":athosp,"death":death,"active":active}
print(covid)

def print_states(**kwargs):
    st=kwargs["state"]
    if st in covid:
        print("State",covid[st]["state"],"\nActive cases:",covid[st]["active"])
        if "death" in kwargs:
            print("State:",covid[st]["state"],"\nDeath:",covid[st]["death"])
        else:
            pass
    else:
        print("Invalid state")


print_states(state="Maharashtra")
