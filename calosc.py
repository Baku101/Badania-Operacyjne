def znajdx_najmniejsze_wiersze(macierz: list[list[int]]) -> list[int]:
    """
    Funkcja znajdująca najmniejszy element w każdym z wierszy macierzy.

    :param macierz: Macierz w wierszach której mają być znalezione najmniejsze elementy.
    :return: Lista najmniejszych elementów w wierszach macierzy.
    """
    najmniejsze_elementy = []
    for wiersz in macierz:
        najmniejszy_element = wiersz[0]
        for element in wiersz[1:]:
            if najmniejszy_element > element:
                najmniejszy_element = element
        najmniejsze_elementy.append(najmniejszy_element)
    return najmniejsze_elementy


def znajdx_najmniejsze_kolumny(macierz: list[list[int]]) -> list[int]:
    """
    Funkcja znajdująca najmniejszy element w każdej z kolumn macierzy.

    :param macierz: Macierz w kolumnach której mają być znalezione najmniejsze elementy.
    :return: Lista najmniejszych elementów w kolumnach macierzy.
    """
    najmniejsze_elementy = []
    for i in range(len(macierz[0])):
        najmniejszy_element = macierz[0][i]
        for j in range(1, len(macierz)):
            if najmniejszy_element > macierz[j][i]:
                najmniejszy_element = macierz[j][i]
        najmniejsze_elementy.append(najmniejszy_element)
    return najmniejsze_elementy


def redukcja_macierzy(macierz: list[list[int]]) -> tuple[list[list[int]], int]:
    """
    Funkcja redukująca podaną macierz.

    :param macierz: Macierz do zredukowania.
    :return: Krotka zawierająca zredukowaną macierz (pierwszy element) oraz wartość dolnego ograniczenia (drugi element).
    """
    # stworzenie kopii redukowanej macierzy
    macierz_kopia = [[element for element in wiersz] for wiersz in macierz]
    # znalezienie w obecnej macierzy najmniejszych elementów w wierszach
    najmniejsze_wiersze = znajdx_najmniejsze_wiersze(macierz_kopia)

    # przejście po każdym wierszu i odjęcie od każdego z jego elementów najmniejszego
    # elementu w obecnym wierszu
    for i in range(len(macierz_kopia[0])):
        for j in range(len(macierz_kopia)):
            # jeżeli najmniejszy element to 0, przejdź do następnego wiersza
            if najmniejsze_wiersze[i] == 0:
                continue
            macierz_kopia[i][j] -= najmniejsze_wiersze[i]

    # znalezienie w obecnej macierzy najmniejszych elementów w wierszach
    najmniejsze_kolumny = znajdx_najmniejsze_kolumny(macierz_kopia)

    # przejście po każdej kolumnie i odjęcie od każdego z jej elementów najmniejszego
    # elementu w obecnej kolumnie
    for j in range(len(macierz_kopia)):
        for i in range(len(macierz_kopia[0])):
            # jeżeli najmniejszy element to 0, przejdź do następnej kolumny
            if najmniejsze_kolumny[j] == 0:
                continue
            macierz_kopia[i][j] -= najmniejsze_kolumny[j]

    # obliczanie dolnego ograniczenia, jako suma elementów w listach najmniejszych elementów
    # w wierszach i kolumnach
    dolne_ograniczenie = sum(najmniejsze_wiersze) + sum(najmniejsze_kolumny)

    return macierz_kopia, dolne_ograniczenie


def wyznaczanie_zer(macierz):
    rz = len(macierz)  # liczba rzędów macierzy
    kol = len(macierz[0])  # liczba kolumn macierzy

    for i in range(rz):  # dla każdego rzędu
        for j in range(kol):  # dla każdej kolumny
            if macierz[i][j] == 0:  # jeśli element jest równy 0
                zero_rz = False
                zero_kol = False
                for k in range(kol):  # d la każdej kolumny
                    if macierz[i][k] == "0*":  # jeśli jest 0* w rzędzie
                        zero_rz = True  # ustawiamy zmienną na True
                        break  # przerywamy pętle
                for k in range(rz):  # dla każdego rzędu
                    if macierz[k][j] == "0*":  # jeśli jest 0* w kolumnie
                        zero_kol = True  # ustawiamy zmienną na True
                        break  # przerywamy pętle
                if not zero_rz and not zero_kol:  # jeśli obie zmienne są na False
                    macierz[i][j] = "0*"  # zero jest niezależne, zamieniamy na 0*
                else:  # jeśli nie
                    macierz[i][j] = "0/"  # zero jest zależne, zamieniamy na 0/
    return macierz

def eliminacja_zer(M):

    zero_niezal = "0*"
    zero_zal = "0/"
    rozmiar = len(M)
    wiersz = [i for i in range(rozmiar)]
    nowy_wiersz = [i for i in range(rozmiar)]
    kolumna = []
    nowa_kolumna = [i for i in range(rozmiar)]
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

    return M


M = [[5, 2, 3, 2, 7],
     [6, 8, 4, 2, 5],
     [6, 4, 3, 7, 2],
     [6, 9, 0, 4, 0],
     [4, 1, 2, 4, 0]]


def main():
    macierz, fi = redukcja_macierzy(M)
    macierz2 = wyznaczanie_zer(macierz)

    for rzad in macierz2:
        print(rzad)
    print()

    macierz3 = eliminacja_zer(macierz2)
    for rzad in macierz3:
        print(rzad)

main()
