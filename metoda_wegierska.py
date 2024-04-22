from setup import *
from redukcja_macierzy import redukcja_macierzy
from wyznaczanie_zer_niezaleznych import wyznaczanie_zer
from eliminacja_zer import eliminacja_zer


def znajdx_przydzial(macierz: Macierz) -> Macierz:
    """
    Funkcja znajdująca przydział dla podanej macierzy z oznaczonymi zerami zależnymi.

    :param macierz: Macierz z oznacznymi zerami zależnymi.
    :return: Macierz binarna reprezentująca optymalny przydział.
    """
    # stwórz nową macierz wypełnioną zerami o takich samych wymiarach jak wejściowa macierz
    nowa_macierz = [[0 for _ in range(len(macierz[0]))] for _ in range(len(macierz))]

    # w nowej macierzy wstaw 1 w każdym miejscu gdzie w macierzy wejściowej jest zero zależne
    for i in range(len(macierz)):
        for j in range(len(macierz[0])):
            if macierz[i][j] == "0*":
                nowa_macierz[i][j] = 1

    # zwróć macierz binarną
    return nowa_macierz


def metoda_wegierska(macierz: Macierz, display: bool = False) -> tuple[Macierz, float]:
    """
    Funkcja realizująca algorytm metody węgierskiej do wyznacznia optymalnego przydziału.

    :param macierz: Macierz opisująca zagadanienie przydzialu.
    :param display: Zmienna, która pozwala na wyświetlenie wczystkich macierzy w obliczeniach.
                    *True* macierze są wyświetlane, *False* macierze nie są wyświetlane. Domyślnie *False*.
    :return: Krotka, której pierwszym elementem jest macierz binarna opisująca optymalny przydział.
             Drugi element to wartość funkcji celu.
    """
    # wstępna redukcja macierzy oraz wyznaczenie początkowego dolnego ograniczenia
    macierz_zredukowana, dolne_ograniczenie = redukcja_macierzy(macierz)
    if display:
        wyswietl_macierz(macierz_zredukowana)
        print("Początkowe dolne ograniczenie:", dolne_ograniczenie, "\n")

    # wyznacznie zer zależnych i niezależnych oraz liczby zer niezależnych
    macierz_z_zerami, liczba_zer_niezal = wyznaczanie_zer(macierz_zredukowana)
    if display:
        wyswietl_macierz(macierz_z_zerami)
        print("Liczba zer niezależnych:", liczba_zer_niezal, "\n")

    # wykonuj pętle while dopóki liczba zer niezależnych jest równa wymiarowi macierzy - n
    while liczba_zer_niezal != len(macierz):

        # wyznacz zbiór niewykreślonych elementów oraz ich indeksów (ne_wierze, ne_kolumny)
        nieskreslone_elementu, ne_wiersze, ne_kolumny = eliminacja_zer(macierz_z_zerami)

        # w przypadku kiedy liczba linii jest równa wymiarowi macierzy zwróć optymalny przydział oraz dolne ograniczenie
        if nieskreslone_elementu is None:
            return znajdx_przydzial(macierz_z_zerami), dolne_ograniczenie

        # wyznacz indeksy skreślonych wierszy
        se_wiersze = [i for i in range(len(macierz[0])) if i not in ne_wiersze]

        # wyznacz indesky skreślonych kolumn
        se_kolumny = [i for i in range(len(macierz)) if i not in ne_kolumny]

        # wyznacz minimalny element ze zbioru niewykreślonych elementów
        minimalny_element = min([min(elementy) for elementy in nieskreslone_elementu])

        # w macierzy zredukowanej odejmij od elementów nieskreślonych wartości minimalnego elementu
        for i in ne_wiersze:
            for j in ne_kolumny:
                macierz_zredukowana[i][j] -= minimalny_element

        # w macierzy zredukowanej dodaj do elementów zakreślonych dwiema liniami wartości minimalnego elementu
        for i in se_wiersze:
            for j in se_kolumny:
                macierz_zredukowana[i][j] += minimalny_element

        # dodanie do dolnego ograniczenia wartości minimalnego elementu
        dolne_ograniczenie += minimalny_element

        # wyznacz nową macierz z oznaczonymi zerami zależnymi, niezależnymi oraz ilość zer niezależnych
        macierz_z_zerami, liczba_zer_niezal = wyznaczanie_zer(macierz_zredukowana)
        if display:
            wyswietl_macierz(macierz_zredukowana)
            print("Dolne ograniczenie:", dolne_ograniczenie, "\n")
            wyswietl_macierz(macierz_z_zerami)
            print("Liczba zer niezależnych:", liczba_zer_niezal, "\n")

    # wyznacz optymalny przydział
    optymalny_przydzial = znajdx_przydzial(macierz_z_zerami)
    if display:
        wyswietl_macierz(optymalny_przydzial)
        print("Dolne ograniczenie:", dolne_ograniczenie, "\n")

    return optymalny_przydzial, dolne_ograniczenie


def main():
    M = [[5, 2, 3, 2, 7],
         [6, 8, 4, 2, 5],
         [6, 4, 3, 7, 2],
         [6, 9, 0, 4, 0],
         [4, 1, 2, 4, 0]]
    M1, phi = metoda_wegierska(M, display=True)
    wyswietl_macierz(M1)
    print("Wartość funkcji celu:", phi)


if __name__ == '__main__':
    main()
