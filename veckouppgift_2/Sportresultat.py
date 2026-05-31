print("Matchen är över, nu ska vi räkna ut resultatet!")
tottenham = int(input("Hur många mål gjorde Tottenham? "))
liverpool =  int(input("Hur många mål gjorde Liverpool? "))


if tottenham >liverpool:
   difference = tottenham - liverpool
   print("Tottenham vann med",difference, "mål!"  )
elif liverpool>tottenham:
   difference = liverpool - tottenham
   print("Liverpool vann med ",difference, "mål!" )
else:
   print("Matchen slutade oavgjort.")
