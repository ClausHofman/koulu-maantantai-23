# print ("moi\nhei")

# for ihminen in ["Keijo", "Kiia", "Vieno", ""]:
#     print("Hei", ihminen)
#     print("Nimessäsi on", len(ihminen), "kirjainta")


# luku = 42
# print("Luku on", luku)

# merkkijono = "Punainen"
# merkkijono2 = "Sininen"

# print("Merkkijonot ovat:", merkkijono, "ja", merkkijono2)

# luku = (1/4/5)*100
# print(type(luku))

# luku = 5
# print(type(luku))

# lista = [
#     "Merkkijono",
#     [1,2,3],
# ]

# sanakirja = {
#     "väri": "punainen",
#     "koko": "pieni",
# }

# print(sanakirja["väri"])

# sanakirja["väri"]="sininen"

# print(sanakirja)

otsikot = [
    {"taso":1, "muotoilu":"ISO","teksti": "opi ohjelmoimaan"},
    {"taso":2, "muotoilu":"Iso alkukirjain","teksti": "Python-ohjelmointi"},
    {"taso":1, "muotoilu":"ISO","teksti": "Elämän tarkoitus"},
    {"taso":2, "muotoilu":"","teksti": "Kuinka löytää elämän tarkoitus?"},
    {"taso":3, "muotoilu":"","teksti": "Mistä tietää?"},
]

for otsikko in otsikot:
    taso = otsikko["taso"]
    sisennys = taso * "    " # Neljä välilyöntiä toistetaan 'taso' kertaa
    teksti = otsikko["teksti"]
    if otsikko["muotoilu"] == "ISO":
        teksti = teksti.upper()
    if otsikko["muotoilu"] == "Iso alkukirjain":
        teksti = teksti.title()
    print(sisennys, teksti)