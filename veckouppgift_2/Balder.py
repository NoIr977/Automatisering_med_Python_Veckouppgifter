min_height = 130


height = float(input("Välkommen, lägg till din längt innan du åker : "))


if height < min_height:
     print("Tyvärr, får du inte åka")
     difference = min_height - height
     print("Du behöver växa " , difference , "cm mer så att kunna åka ")


else:
   print("Grattis! Du får Åka! ")


 #Varför just tre värden?
 #Tre värden används för att testa olika situationer: ett värde under gränsen, ett på gränsen och ett över gränsen.
#Varför dessa värden?
 #121 cm är gränsvärdet. Ett lägre värde visar att personen inte får åka, och ett högre värde visar att personen får åka. På så sätt testar man att programmet fungerar korrekt.
#Skulle det vara bra att lägga till testvärdet 129 cm?
 #Ja, det kan vara bra. 129 cm ligger nära gränsen och hjälper till att kontrollera att programmet hanterar värden runt gränsen på rätt sätt.