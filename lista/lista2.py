print(" Nevek 'vege' névjelig")

nev = "null"
nevek = []
while nev != "vege":  #sor végére kell írni hogy vege addig fut
    nev = input("Név: ")
    nevek.append(nev)

for nevElem in nevek:
    print(nevElem)