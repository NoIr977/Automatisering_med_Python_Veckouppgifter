temp_cels = float(input("Ange temperatur i Celsius: "))
temp_fahr = float(1.8 * temp_cels + 32)
print("Det blir" , temp_fahr, "grader i Fahrenheit")

temperature = input("Ange om du vill ha temperaturen i Celsius (C) eller Fahrenheit (F): ")


if temperature == str("C"):
    print("Bra vi ska räkna temperaturen i Celsius")
    fahr_to_cels = float(input("Ange temperaturen i Farhenheit så att veta temperaturen i Celsius: "))
    cels = (fahr_to_cels - 32) / 1.8
    print("Temperaturen i Celsius är ", cels, "grader ")

else:
    print("Bra vi ska räkna temperaturen i Fahrenheit")
    cels_to_fahr = float(input("Ange temperatur i Celsius så att veta temperaturen i Fahrenheit: "))
    fahr = float(1.8 * cels_to_fahr + 32)
    print("Temperaturen i Celsius är ", fahr, "grader ")

if cels >=20:
    print("Det är dags att packa badklöder")
else:
    print("Det är kalt ute, glöm inte att ta varmkläder")



