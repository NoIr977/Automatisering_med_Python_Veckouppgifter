
print("Välkommen till gissa talet spel! Jag tänker på ett tal mellan 1 och 100. Kan du gissa vilket det är? ")
tal = 40
while True:
    gissa = float(input("Gissa: "))

    if gissa == tal:
     print("Helt rätt! Svaret är: ", tal, "Grattis!")
     break

    if gissa >=35 and gissa <=45: (
     print("Nu börjar det brinna!"))

    if gissa < tal:
          print("Nej, det är för lågt! Gissa igen!")

    if gissa > tal:
        print("Nej, det är för högt! Gissa igen!")


