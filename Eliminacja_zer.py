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
    if linie == rozmiar:
        return "Liczba linii odpowiada wielkości macierzy"






