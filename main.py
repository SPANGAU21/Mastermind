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
i=0
x = 0
svar = []
if svårhetsnivå == "lätt":
    while i <4:
        r = random.randint(1,6)
        svar.append(r) 
        for a in range(i):
            if svar[i] == svar[a]:
                svar.pop(i)
                i -= 1
                break
        i+=1

elif svårhetsnivå == "svårt":
    while i < 4:
        svar.append(random.randint(1,6))                  
        i+=1
print(svar)
                


i=0
while i <=12:
    try:
        gissning = input("Ange gissning som följd av fyra tal mellan 1 och 6, t.ex. 1234:").replace(" ","")
        if len(gissning) != 4:
            print("Du måste ange exakt fyra siffror!")
            continue
        elif not all(char in '123456' for char in gissning):
            print("Du måste ange siffror mellan 1 och 6!")
            continue
    except ValueError:
        print("Ett fel uppstod")
        continue
          
