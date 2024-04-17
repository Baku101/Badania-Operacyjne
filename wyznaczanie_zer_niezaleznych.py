# wyznaczanie zer niezależnych 

macierz = [
    [0, 0, 1, 0, 5],
    [1, 6, 2, 0, 3],
    [1, 2, 1, 5, 0],
    [3, 9, 0, 4, 0],
    [1, 1, 2, 4, 0]
]

def wyznaczanie_zer(macierz):

    rz = len(macierz)           #liczba rzędów macierzy
    kol = len(macierz[0])       #liczba kolumn macierzy

    for i in range(rz):         #dla każdego rzędu
        for j in range(kol):    #dla każdej kolumny
            if macierz[i][j] == 0:      #jeśli element jest równy 0
                    zero_rz = False    
                    zero_kol = False
                    for k in range(kol):        #dla każdej kolumny
                        if macierz[i][k] == "0*":   #jeśli jest 0* w rzędzie
                            zero_rz = True      #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    for k in range(rz):         #dla każdego rzędu
                        if macierz[k][j] == "0*":   #jeśli jest 0* w kolumnie 
                            zero_kol = True         #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    if not zero_rz and not zero_kol:    #jeśli obie zmienne są na False
                        macierz[i][j] = "0*"        #zero jest niezależne, zamieniamy na 0*
                    else:                       #jeśli nie
                        macierz[i][j] = "0/"        #zero jest zależne, zamieniamy na 0/
    return macierz

macierz = wyznaczanie_zer(macierz)
for rzad in macierz:
    print(rzad)
