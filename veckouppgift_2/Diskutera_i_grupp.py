is_member = False
level_1 = 100
level_2 = 300
price = float(input("Välkommen, köp något dyrt : " ))


if price >= level_1:
   print("Grattis du är avancerat till nivå 1 och får 10% " )
   discount = 10


elif price >= level_2:
       print("Grattis! Du har avavncerat till nivå 2 och får 25% rabatt . ")
       discount =  25
else:
       discount = 0
       print("Ingen rabatt. ")




final_price = price * (100 - discount) / 100


print ("Efter rabatter blir priset ... ", final_price)