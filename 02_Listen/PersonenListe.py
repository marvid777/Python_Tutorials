Personen =[]


def Person_eingabe():
    hvPerson = []
    vname = input("Vorname ? ")
    nname = input("Nachname ? ")

    hvPerson.append(vname)
    hvPerson.append(nname)

    return hvPerson



Personen.append(Person_eingabe())

#Person_eingabe()
#Person_eingabe()
#Person_eingabe()



def max(a,b):
    nv = 0
    if a>b:
        nv = a
    else:
        nv = b
    return nv

print(max(4,9))
