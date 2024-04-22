import numpy as np

# alias na typ reprezentujący macierz
Macierz = list[list[int | float]]


# funkcja wykorzystująca wyświetlanie w numpy do wyświetlania macierzy
def wyswietl_macierz(macierz: Macierz) -> None:
    print(np.array(macierz))
