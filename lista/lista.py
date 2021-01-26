
hok = [7.5, 5.8, 2.7]


print("első: ", hok[0])

hok2 = [7.5, 5.8, 2.7]

if hok==hok2:
    print("egyenlő")

print(len(hok2))

for ho in hok:
    print("hőmérséklet: ", ho)

nevek = "Béla", "Lajos", "Zoli"

if "Béla" in nevek:
    print("szopki Béla")

voltFagy = False
for ho in hok:
    if ho < 0:
        voltFagy = True

if voltFagy:
    print("volt fagy")
else:
    print("nem volt fagy")