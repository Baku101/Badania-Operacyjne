# wyznaczanie zer niezależnych 

macierz = [
    [0, 0, 1, 0, 5],
    [1, 6, 2, 0, 3],
    [1, 2, 1, 5, 0],
    [3, 9, 0, 4, 0],
    [1, 1, 2, 4, 0]
]

def wyznaczanie_zer(macierz,fi):

    rz = len(macierz)
    kol = len(macierz[0])

    for i in range(rz):
        for j in range(kol):
            if macierz[i][j] == 0:
                    zero_rz = False
                    zero_kol = False
                    for k in range(kol):
                        if macierz[i][k] == "0*":
                            zero_rz = True
                            break
                    for k in range(rz):
                        if macierz[k][j] == "0*":
                            zero_kol = True
                            break
                    if not zero_rz and not zero_kol:
                        macierz[i][j] = "0*"
                    else:
                        macierz[i][j] = "0/"
    return macierz

fi = 0
macierz = wyznaczanie_zer(macierz,fi)
for rzad in macierz:
    print(rzad)