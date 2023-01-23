

def kysy_nimi():
    nimi = input("Anna nimi: ")
    return nimi

# joku = kysy_nimi()
# print(joku)


def kysy_nimet(lkm):
    nimet = []
    while len(nimet) < lkm:
        nimi = kysy_nimi()
        nimet.append(nimi)
    return nimet

if __name__ == "__main__":
    nimilista = kysy_nimet(3)
    print(nimilista)

