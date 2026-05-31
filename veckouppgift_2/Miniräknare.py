tal1 = float(input("Ange första tal: "))
tal2 = float(input("Ange andra tal: "))
tal3 = float(input("Ange tredje tal: "))


summa = tal1+tal2+tal3
print("Summan av alla tre tal är: ", summa)


if tal1>tal2 and tal2>tal3:
   print("Första tal är den storsta ")


elif tal1<tal2 and tal2>tal3:
   print("Andra tal är den storsta ")


elif tal1==tal2 or tal2==tal3:
   print("Finns inga storre tal ")


else:
   print("Tradje tal är den storsta")




if tal1==tal2 and tal2==tal3:
   print("Alla tre tal är lika")
elif tal1 == tal2 and tal2 != tal3:
   print("Första och Andra tal är lika")
elif tal1 != tal2 and tal2== tal3:
   print("Andra och tredje tal är lika")






if tal1 == tal2 == tal3:
   print("Alla tal är lika:", tal1)


# если есть одинаковые (НО не все три)
elif tal1 == tal2 or tal1 == tal3 or tal2 == tal3:
   print("Finns inget mellersta tal")


# если все разные
else:
   mellerst = sorted([tal1, tal2, tal3])[1]
   print("Mellersta talet är", mellerst)