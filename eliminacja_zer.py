# Algorytm wyznaczający minimalny zbiór linii wykreślających wszystkie zera z macierzy.
# Macierz = list(list)
def eliminacja_zer(M):

    zero_niezal = "0*"
    zero_zal = "0/"
    rozmiar = len(M)
    wiersz = [i for i in range(rozmiar)]
    kolumna = []
    linie = 0

    # 1. Poszukiwanie maksymalnego skojarzenia
    # 1a. Oznaczyć każdy wiersz nieposiadający niezależnego 0
    for i in range(rozmiar):
        for j in range(rozmiar):
            if M[i][j] == zero_niezal:
                wiersz.remove(i)
                linie += 1
    # 1b. Oznaczyć każdą kolumnę posiadającą zależne 0 w oznaczonym wierszu
    for i in wiersz:
        for j in range(rozmiar):
            if M[i][j] == zero_zal:
                kolumna.append(j)
                linie += 1
    # 1c. Oznaczyć każdy wiersz posiadający niezależne 0 w oznaczonej kolumnie
    for i in range(rozmiar):
        for j in kolumna:
            if M[i][j] == zero_niezal:
                wiersz.append(i)
                linie += 1
    # Wypadek, w którym liczba linii kryjących wartości jest równa liczbie zer niezależnych
    if linie == rozmiar:
        return "Liczba linii odpowiada wielkości macierzy"
    # Usuwanie kolumn
    M = [[rzad[i] for i in range(rozmiar) if i not in kolumna] for rzad in M]
    # Usuwanie wierszy
    M = [rzad for index, rzad in enumerate(M) if index in wiersz]
    # Indeks usuniętych wierszy
    usun_wiersz = [i for i in range(rozmiar) if i in wiersz]
    usun_kolumna = [i for i in range(rozmiar) if i not in kolumna]
    
    return M, usun_wiersz, usun_kolumna


M = [['0*', '0/', 1, '0/', 5],
     [1, 6, 2, '0*', 3],
     [1, 2, 1, 5, '0*'],
     [3, 9, '0*', 4, '0/'],
     [1, 1, 2, 4, '0/']]


def main():
    macierz, wiersz, kolumna = eliminacja_zer(M)
    for rzad in macierz:
        print(rzad)
    print(wiersz)
    print(kolumna)


main()
