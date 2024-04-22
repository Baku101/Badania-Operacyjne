from setup import *


def znajdx_najmniejsze_wiersze(macierz: Macierz) -> list[float]:
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


def znajdx_najmniejsze_kolumny(macierz: Macierz) -> list[float]:
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


def redukcja_macierzy(macierz: Macierz) -> tuple[Macierz, float]:
    """
    Funkcja redukująca podaną macierz.

    :param macierz: Macierz do zredukowania.
    :return: Krotka zawierająca zredukowaną macierz (pierwszy element) oraz wartość dolnego ograniczenia (drugi element).
    """
    # stworzenie kopii redukowanej macierzy
    macierz_kopia = [[element for element in wiersz] for wiersz in macierz]
    # znalezienie w obecnej macierzy najmniejszych elementów w wierszach
    najmniejsze_wiersze = znajdx_najmniejsze_wiersze(macierz_kopia)

    # przejście po każdym wierzu i odjęcie od każdego z jego elementów najmniejszego
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


def main():
    M = [[5, 2, 3, 2, 7],
         [6, 8, 4, 2, 5],
         [6, 4, 3, 7, 2],
         [6, 9, 0, 4, 0],
         [4, 1, 2, 4, 0]]
    print(znajdx_najmniejsze_wiersze(M), "\n")
    print(znajdx_najmniejsze_kolumny(M), "\n")
    M_zredukowanie, dolne_ograniczenie = redukcja_macierzy(M)
    print(M_zredukowanie, "\n")
    print(dolne_ograniczenie)


if __name__ == "__main__":
    main()
