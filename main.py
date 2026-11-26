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
    except ValueError:
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
                
rätt_plats=0
rätt_gissat=0
i=0
while i <=12:
    try:
        gissning = input("Ange gissning som följd av fyra tal:").replace(" ","")
        if len(gissning) != 4:
            print("Du måste ange exakt fyra siffror!")
            continue
        elif not all(char in '123456' for char in gissning):
            print("Du måste ange siffror mellan 1 och 6!")
            continue
    except ValueError:
        print("Ett fel uppstod")
        continue
    gissning = [int(x) for x in gissning]

    if gissning == svar:
        print("Grattis du van!")
        print("Koden var:",svar,"!")
        while True:
            try:
                spela_igen=input("vill du spela igen?").lower().replace(" ","")
                if spela_igen == "nej":
                    print("Tack för att du spela")
                    break
                elif spela_igen == "ja":
                    ändra_svårhetsnivå = input("Vill du ändra svårhetsnivå?")
                    if ändra_svårhetsnivå == "ja":
                        while True:
                            try:
                                svårhetsnivå = input("Ange önskad nivå: lätt/svårt:").lower().replace(" ","")
                                if svårhetsnivå == "lätt":
                                    break
                                elif svårhetsnivå == "svårt":
                                    break
                                else:
                                    print("Svara bara lätt eller svårt!")
                            except ValueError:
                                print("Ett fel uppstod, försök igen")
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
                    i=0
                    rätt_plats=0
                    rätt_gissat=0
            except ValueError:
                print("Något gick fel")

                    
                
                    
                         


    for b in range(4):
        if gissning[b] == svar[b]:
            rätt_plats += 1

        elif gissning[b] in svar:
            rätt_gissat += 1

    print("✅"*rätt_plats,"🔲"*rätt_gissat)
    i+=1
    rätt_plats=0
    rätt_gissat=0

