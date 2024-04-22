from setup import *
# wyznaczanie zer niezależnych


def wyznaczanie_zer(macierz: Macierz) -> tuple[Macierz, int]:
    macierz_kopia = [[element for element in wiersz] for wiersz in macierz]
    macierz_kopia2 = [[element for element in wiersz] for wiersz in macierz]
    rz = len(macierz)           #liczba rzędów macierzy
    kol = len(macierz[0])       #liczba kolumn macierzy
    liczba_zer_niezal = 0
    liczba_zer_niezal2 = 0

    for i in range(rz):         #dla każdego rzędu
        for j in range(kol):    #dla każdej kolumny
            if macierz_kopia[i][j] == 0:      #jeśli element jest równy 0
                    zero_rz = False
                    zero_kol = False
                    for k in range(kol):        #dla każdej kolumny
                        if macierz_kopia[i][k] == "0*":   #jeśli jest 0* w rzędzie
                            zero_rz = True      #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    for k in range(rz):         #dla każdego rzędu
                        if macierz_kopia[k][j] == "0*":   #jeśli jest 0* w kolumnie
                            zero_kol = True         #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    if not zero_rz and not zero_kol:    #jeśli obie zmienne są na False
                        macierz_kopia[i][j] = "0*"      #zero jest niezależne, zamieniamy na 0*
                        liczba_zer_niezal += 1
                    else:                       #jeśli nie
                        macierz_kopia[i][j] = "0/"        #zero jest zależne, zamieniamy na 0/


    for i in reversed(range(rz)):
        for j in range(kol):   #dla każdej kolumny
            if macierz_kopia2[i][j] == 0:      #jeśli element jest równy 0
                    zero_rz = False
                    zero_kol = False
                    for k in range(kol):        #dla każdej kolumny
                        if macierz_kopia2[i][k] == "0*":   #jeśli jest 0* w rzędzie
                            zero_rz = True      #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    for k in range(rz):         #dla każdego rzędu
                        if macierz_kopia2[k][j] == "0*":   #jeśli jest 0* w kolumnie
                            zero_kol = True         #ustawiamy zmienną na True
                            break               #przerywamy pętle
                    if not zero_rz and not zero_kol:    #jeśli obie zmienne są na False
                        macierz_kopia2[i][j] = "0*"      #zero jest niezależne, zamieniamy na 0*
                        liczba_zer_niezal2 += 1
                    else:                       #jeśli nie
                        macierz_kopia2[i][j] = "0/"        #zero jest zależne, zamieniamy na 0/

    if liczba_zer_niezal >= liczba_zer_niezal2:
        return macierz_kopia, liczba_zer_niezal
    else: 
        return macierz_kopia2, liczba_zer_niezal2


def main():
    macierz = [[0, 0, 1, 0, 5],
               [1, 6, 2, 0, 3],
               [1, 2, 1, 5, 0],
               [3, 9, 0, 4, 0],
               [1, 1, 2, 4, 0]]
    macierz2 = [[0, 0, 1, 0, 6],
               [1, 6, 2, 0, 4],
               [0, 1, 0, 4, 0],
               [3, 9, 0, 4, 1],
               [0, 0, 1, 3, 0]]
    macierz, licz_zer_niezal = wyznaczanie_zer(macierz2)
    for rzad in macierz:
        print(rzad)
    print(licz_zer_niezal)

if __name__ == '__main__':
    main()
