total = 0


print("Skriv ett tal for att räkna ut en summan, när du är redo att veta summan, skriv quit.")
while True:
    value = input("Skriv in ett tal: ")
    if value == "quit" :
        break

    total += int(value)

print("Nu ska vi räkna hur många värja gruppmedlem ska betala: ")

person= int(input("Hur många persion är i gruppen: "))

total1 = (total/ person)

print("Summan av alla dina tal är" , total,"sek.,",  "och varje gruppmedlem ska betala:" , total1, "sek.")


driks = input("Vill du lämna driks? (YES/NO)")

if driks == "YES":
    tip = float(input("Hur mycket pengar vill du lämna: "))
    money_total = tip+total
    print("Tack då ska du betala till oss idag: ", money_total)

else:
    tip = (total*0.10) +total
print("Totalt att betala: ", tip, "kr")



for a in range(1,7):
    s = ""
    for f in range (1, 9):
        if 3<=f <=6:
            s+= "#"
            if 5<=f:
              s+="*"
        else:
            s += "."
            print(s)