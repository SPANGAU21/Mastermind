import random

print("Datorn kommer att slumpa fram en kod på fyra siffror mellan 1 och 6.")
print("Du ska försöka gissa denna kods siffror på max 12 drag.")
print("Efter respektiv gissning så kommer du få en respons:")
print("För varje gissad korrekt på korrekt plats i koden:✅")
print("För varje gissad korrekt på fel plats i koden:🔲")
print("För de siffror som inte finns i koden ges ingen markering.")
print(" ")
print("Exempel: om den slumpade koden är 2315")
print("och du gissar 3165")
print("så blir responsen ✅🔲🔲")
print(" ")
print("Du får välja mellan två svårhetsnivåer:")
print("Lättare nivå: Alla siffror är garanterat olika")
print("Svårare nivå: Det kan finnas upprepningar av olika eller flera siffror")
print(" ")

while True:
    try:
        svårhetsnivå = input("Ange önskad nivå: lätt/svårt:").lower().replace(" ","")
        if svårhetsnivå == "lätt":
            break
        elif svårhetsnivå == "svårt":
            break
        else:
            print("Svara bara lätt eller svårt!")
    except Exception as e:
        print("Ett fel uppstod, försök igen")

