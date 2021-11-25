import sys

print(sys.argv)

# Vstupní proměnné
oddelovac = "*" * 40

rozbor_textu1 = {}
rozbor_textu2 = {}
rozbor_textu3 = {}


text1 = '''
Situated about 10 miles west of Kemmerer, 
Fossil Butte is a ruggedly impressive 
topographic feature that rises sharply 
some 1000 feet above Twin Creek Valley 
to an elevation of more than 7500 feet 
above sea level. The butte is located just 
north of US 30N and the Union Pacific Railroad, 
which traverse the valley. '''
text2 = '''
At the base of Fossil Butte are the bright 
red, purple, yellow and gray beds of the Wasatch 
Formation. Eroded portions of these horizontal 
beds slope gradually upward from the valley floor 
and steepen abruptly. Overlying them and extending 
to the top of the butte are the much steeper 
buff-to-white beds of the Green River Formation, 
which are about 300 feet thick.'''
text3 = '''
The monument contains 8198 acres and protects 
a portion of the largest deposit of freshwater fish 
fossils in the world. The richest fossil fish deposits 
are found in multiple limestone layers, which lie some 
100 feet below the top of the butte. The fossils 
represent several varieties of perch, as well as 
other freshwater genera and herring similar to those 
in modern oceans. Other fish such as paddlefish, 
garpike and stingray are also present.'''


registrovani = {"bob": "123", "ann": "pass123", "mike": "password123", "liz": "pass123"}

# Zadání od uživatele
uzivatel = input("Zadejte uživatelské jméno: ")
heslo = input("Zadejte heslo: ")
print(f"Uživatelské jméno: {uzivatel}")
print(f"Heslo: {heslo}")
print(oddelovac)

# Podmínka pro registrované uživatele
if heslo == registrovani.get(uzivatel):
    print(f"Vítejte {uzivatel},máme pro Vás 3 texty k analýze.")

else:
    print("Neznámý uživatel, ukončuji program.")
    quit()
print(oddelovac)

for cislo, text in enumerate([text1], 1):
            cista_slova = [slovo.strip(".,\n") for slovo in text.split()]
            rozbor_textu1[f"text:{cislo}"] = {"Počet slov ve vybraném textu": len(text.split()),
                                              "Počet slov začínajících na velké písmeno": len([slovo1 for slovo1 in cista_slova if slovo1.istitle()]),
                                              "Počet slov psaných velkým písmenem": len([slovo2 for slovo2 in cista_slova if slovo2.isupper()]),
                                              "Počet slov psaných malými písmeny": len([slovo3 for slovo3 in cista_slova if slovo3.islower()]),
                                              "Počet čísel": len([slovo4 for slovo4 in cista_slova if slovo4.isnumeric()]),
                                              "Součet čísel:": sum([int(slovo5) for slovo5 in cista_slova if slovo5.isdigit()])
                                              }

for cislo, text in enumerate([text2], 2):
            cista_slova = [slovo.strip(".,\n") for slovo in text.split()]
            rozbor_textu2[f"text:{cislo}"] = {"Počet slov ve vybraném textu": len(text.split()),
                                              "Počet slov začínajících na velké písmeno": len([slovo6 for slovo6 in cista_slova if slovo6.istitle()]),
                                              "Počet slov psaných velkým písmenem": len([slovo7 for slovo7 in cista_slova if slovo7.isupper()]),
                                              "Počet slov psaných malými písmeny": len([slovo8 for slovo8 in cista_slova if slovo8.islower()]),
                                              "Počet čísel": len([slovo9 for slovo9 in cista_slova if slovo9.isnumeric()]),
                                              "Součet čísel:": sum([int(slovo10) for slovo10 in cista_slova if slovo10.isdigit()])}


for cislo, text in enumerate([text3], 3):
            cista_slova = [slovo.strip(".,\n") for slovo in text.split()]
            rozbor_textu3[f"text:{cislo}"] = {"Počet slov ve vybraném textu": len(text.split()),
                                              "Počet slov začínajících na velké písmeno": len([slovo11 for slovo11 in cista_slova if slovo11.istitle()]),
                                              "Počet slov psaných velkým písmenem": len([slovo12 for slovo12 in cista_slova if slovo12.isupper()]),
                                              "Počet slov psaných malými písmeny": len([slovo13 for slovo13 in cista_slova if slovo13.islower()]),
                                              "Počet čísel": len([slovo14 for slovo14 in cista_slova if slovo14.isnumeric()]),
                                              "Součet čísel:": sum([int(slovo15) for slovo15 in cista_slova if slovo15.isdigit()])}



vyber = int(input("Zadej číslo textu od 1 do 3: "))
print(oddelovac)

if vyber == 1:
    print(rozbor_textu1)
elif vyber == 2:
    print(rozbor_textu2)
elif vyber == 3:
    print(rozbor_textu3)
else:
    print("Zadali jste špatné číslo.")
    quit()


if vyber ==1:
        cista_slova = [i.strip(".,\n") for i in text1.split()]

        s1 = [str(i) for i in cista_slova if len(i) == 1]
        s2 = [str(i) for i in cista_slova if len(i) == 2]
        s3 = [str(i) for i in cista_slova if len(i) == 3]
        s4 = [str(i) for i in cista_slova if len(i) == 4]
        s5 = [str(i) for i in cista_slova if len(i) == 5]
        s6 = [str(i) for i in cista_slova if len(i) == 6]
        s7 = [str(i) for i in cista_slova if len(i) == 7]
        s8 = [str(i) for i in cista_slova if len(i) == 8]
        s9 = [str(i) for i in cista_slova if len(i) == 9]
        s10 = [str(i) for i in cista_slova if len(i) == 10]
        s11 = [str(i) for i in cista_slova if len(i) == 11]

        poradi1 = "1|"
        poradi2 = "2|"
        poradi3 = "3|"
        poradi4 = "4|"
        poradi5 = "5|"
        poradi6 = "6|"
        poradi7 = "7|"
        poradi8 = "8|"
        poradi9 =  "9|"
        poradi10 = "10|"
        poradi11 = "11|"

        vyskyt1 = "*" * len(s1)
        vyskyt2 = "*" * len(s2)
        vyskyt3 = "*" * len(s3)
        vyskyt4 = "*" * len(s4)
        vyskyt5 = "*" * len(s5)
        vyskyt6 = "*" * len(s6)
        vyskyt7 = "*" * len(s7)
        vyskyt8 = "*" * len(s8)
        vyskyt9 = "*" * len(s9)
        vyskyt10 = "*" * len(s10)
        vyskyt11 = "*" * len(s11)

        cislo1 = ("|" + str(len(s1)))
        cislo2 = ("|" + str(len(s2)))
        cislo3 = ("|" + str(len(s3)))
        cislo4 = ("|" + str(len(s4)))
        cislo5 = ("|" + str(len(s5)))
        cislo6 = ("|" + str(len(s6)))
        cislo7 = ("|" + str(len(s7)))
        cislo8 = ("|" + str(len(s8)))
        cislo9 = ("|" + str(len(s9)))
        cislo10 = ("|" + str(len(s10)))
        cislo11 = ("|" + str(len(s11)))

        print(oddelovac)
        poradi = "POŘ|"
        vyskyt = "VÝSKYT"
        cislo = "|ČÍSLO"
        print(f"{poradi : <3}{vyskyt : ^20}{cislo : >3}")
        print(oddelovac)
        print(f"{poradi1 : >4}{vyskyt1 : <20}{cislo1 : >2}")
        print(f"{poradi2 : >4}{vyskyt2 : <20}{cislo2 : >2}")
        print(f"{poradi3 : >4}{vyskyt3 : <20}{cislo3 : >2}")
        print(f"{poradi4 : >4}{vyskyt4 : <20}{cislo4 : >2}")
        print(f"{poradi5 : >4}{vyskyt5 : <20}{cislo5 : >2}")
        print(f"{poradi6 : >4}{vyskyt6 : <20}{cislo6 : >2}")
        print(f"{poradi7 : >4}{vyskyt7 : <20}{cislo7 : >2}")
        print(f"{poradi8 : >4}{vyskyt8 : <20}{cislo8 : >2}")
        print(f"{poradi9 : >4}{vyskyt9 : <20}{cislo9 : >2}")
        print(f"{poradi10 : >4}{vyskyt10 : <20}{cislo10 : >2}")
        print(f"{poradi11 : >4}{vyskyt11 : <20}{cislo11 : >2}")

elif vyber == 2:
        cista_slova = [i.strip(".,\n") for i in text2.split()]

        s1 = [str(i) for i in cista_slova if len(i) == 1]
        s2 = [str(i) for i in cista_slova if len(i) == 2]
        s3 = [str(i) for i in cista_slova if len(i) == 3]
        s4 = [str(i) for i in cista_slova if len(i) == 4]
        s5 = [str(i) for i in cista_slova if len(i) == 5]
        s6 = [str(i) for i in cista_slova if len(i) == 6]
        s7 = [str(i) for i in cista_slova if len(i) == 7]
        s8 = [str(i) for i in cista_slova if len(i) == 8]
        s9 = [str(i) for i in cista_slova if len(i) == 9]
        s10 = [str(i) for i in cista_slova if len(i) == 10]
        s11 = [str(i) for i in cista_slova if len(i) == 11]

        poradi1 = "1|"
        poradi2 = "2|"
        poradi3 = "3|"
        poradi4 = "4|"
        poradi5 = "5|"
        poradi6 = "6|"
        poradi7 = "7|"
        poradi8 = "8|"
        poradi9 = "9|"
        poradi10 = "10|"
        poradi11 = "11|"

        vyskyt1 = "*" * len(s1)
        vyskyt2 = "*" * len(s2)
        vyskyt3 = "*" * len(s3)
        vyskyt4 = "*" * len(s4)
        vyskyt5 = "*" * len(s5)
        vyskyt6 = "*" * len(s6)
        vyskyt7 = "*" * len(s7)
        vyskyt8 = "*" * len(s8)
        vyskyt9 = "*" * len(s9)
        vyskyt10 = "*" * len(s10)
        vyskyt11 = "*" * len(s11)

        cislo1 = ("|" + str(len(s1)))
        cislo2 = ("|" + str(len(s2)))
        cislo3 = ("|" + str(len(s3)))
        cislo4 = ("|" + str(len(s4)))
        cislo5 = ("|" + str(len(s5)))
        cislo6 = ("|" + str(len(s6)))
        cislo7 = ("|" + str(len(s7)))
        cislo8 = ("|" + str(len(s8)))
        cislo9 = ("|" + str(len(s9)))
        cislo10 = ("|" + str(len(s10)))
        cislo11 = ("|" + str(len(s11)))

        print(oddelovac)
        poradi = "POŘ|"
        vyskyt = "VÝSKYT"
        cislo = "|ČÍSLO"
        print(f"{poradi : <3}{vyskyt : ^20}{cislo : >3}")
        print(oddelovac)
        print(f"{poradi1 : >4}{vyskyt1 : <20}{cislo1 : >2}")
        print(f"{poradi2 : >4}{vyskyt2 : <20}{cislo2 : >2}")
        print(f"{poradi3 : >4}{vyskyt3 : <20}{cislo3 : >2}")
        print(f"{poradi4 : >4}{vyskyt4 : <20}{cislo4 : >2}")
        print(f"{poradi5 : >4}{vyskyt5 : <20}{cislo5 : >2}")
        print(f"{poradi6 : >4}{vyskyt6 : <20}{cislo6 : >2}")
        print(f"{poradi7 : >4}{vyskyt7 : <20}{cislo7 : >2}")
        print(f"{poradi8 : >4}{vyskyt8 : <20}{cislo8 : >2}")
        print(f"{poradi9 : >4}{vyskyt9 : <20}{cislo9 : >2}")
        print(f"{poradi10 : >4}{vyskyt10 : <20}{cislo10 : >2}")
        print(f"{poradi11 : >4}{vyskyt11 : <20}{cislo11 : >2}")

elif vyber == 3:
        cista_slova = [i.strip(".,\n") for i in text3.split()]

        s1 = [str(i) for i in cista_slova if len(i) == 1]
        s2 = [str(i) for i in cista_slova if len(i) == 2]
        s3 = [str(i) for i in cista_slova if len(i) == 3]
        s4 = [str(i) for i in cista_slova if len(i) == 4]
        s5 = [str(i) for i in cista_slova if len(i) == 5]
        s6 = [str(i) for i in cista_slova if len(i) == 6]
        s7 = [str(i) for i in cista_slova if len(i) == 7]
        s8 = [str(i) for i in cista_slova if len(i) == 8]
        s9 = [str(i) for i in cista_slova if len(i) == 9]
        s10 = [str(i) for i in cista_slova if len(i) == 10]
        s11 = [str(i) for i in cista_slova if len(i) == 11]

        poradi1 = "1|"
        poradi2 = "2|"
        poradi3 = "3|"
        poradi4 = "4|"
        poradi5 = "5|"
        poradi6 = "6|"
        poradi7 = "7|"
        poradi8 = "8|"
        poradi9 = "9|"
        poradi10 = "10|"
        poradi11 = "11|"

        vyskyt1 = "*" * len(s1)
        vyskyt2 = "*" * len(s2)
        vyskyt3 = "*" * len(s3)
        vyskyt4 = "*" * len(s4)
        vyskyt5 = "*" * len(s5)
        vyskyt6 = "*" * len(s6)
        vyskyt7 = "*" * len(s7)
        vyskyt8 = "*" * len(s8)
        vyskyt9 = "*" * len(s9)
        vyskyt10 = "*" * len(s10)
        vyskyt11 = "*" * len(s11)

        cislo1 = ("|" + str(len(s1)))
        cislo2 = ("|" + str(len(s2)))
        cislo3 = ("|" + str(len(s3)))
        cislo4 = ("|" + str(len(s4)))
        cislo5 = ("|" + str(len(s5)))
        cislo6 = ("|" + str(len(s6)))
        cislo7 = ("|" + str(len(s7)))
        cislo8 = ("|" + str(len(s8)))
        cislo9 = ("|" + str(len(s9)))
        cislo10 = ("|" + str(len(s10)))
        cislo11 = ("|" + str(len(s11)))

        print(oddelovac)
        poradi = "POŘ|"
        vyskyt = "VÝSKYT"
        cislo = "|ČÍSLO"
        print(f"{poradi : <2}{vyskyt : ^20}{cislo : >3}")
        print(oddelovac)
        print(f"{poradi1 : >4}{vyskyt1 : <20}{cislo1 : >2}")
        print(f"{poradi2 : >4}{vyskyt2 : <20}{cislo2 : >2}")
        print(f"{poradi3 : >4}{vyskyt3 : <20}{cislo3 : >2}")
        print(f"{poradi4 : >4}{vyskyt4 : <20}{cislo4 : >2}")
        print(f"{poradi5 : >4}{vyskyt5 : <20}{cislo5 : >2}")
        print(f"{poradi6 : >4}{vyskyt6 : <20}{cislo6 : >2}")
        print(f"{poradi7 : >4}{vyskyt7 : <20}{cislo7 : >2}")
        print(f"{poradi8 : >4}{vyskyt8 : <20}{cislo8 : >2}")
        print(f"{poradi9 : >4}{vyskyt9 : <20}{cislo9 : >2}")
        print(f"{poradi10 : >4}{vyskyt10 : <20}{cislo10 : >2}")
        print(f"{poradi11 : >4}{vyskyt11 : <20}{cislo11 : >2}")
else:
    print("Zadali jste nesprávné číslo, konec programu.")
    quit()
