mname = input ("Wie ist dein Name ")


alter  = int(input ("Wie bist du "))
print ("Hallo ", mname, " und Du bist ", alter,  " Jahre alt")

if alter < 18:
    print("Du bist sicher noch in der Schule")

# if 18 < alter < 25:
#    print("Du studierst gerade")

elif alter < 25:
    print("Du studierst gerade")

else:
    print("Du bist ganz schön alt !!!")


