def rysuj_trojkat_z_odbiciem(wysokosc):
    """
    Funkcja rysująca trójkąt równoboczny o podanej wysokości wraz z jego odbiciem lustrzanym, używając gwiazdek.
    """

    # Sprawdź poprawność wysokości
    if wysokosc <= 0:
        print("Wysokość musi być dodatnią liczbą całkowitą!")
        return

    # Rysowanie górnej części trójkąta
    for i in range(wysokosc):
        liczba_spacji = wysokosc - i - 1
        liczba_gwiazdek = 2 * i + 1

        print(" " * liczba_spacji, end="")
        print("*" * liczba_gwiazdek)

    # Rysowanie dolnej części trójkąta (odbicie lustrzane)
    for i in range(wysokosc - 1, -1, -1):  # Pętla w odwrotnej kolejności
        liczba_spacji = wysokosc - i - 1
        liczba_gwiazdek = 2 * i + 1

        print(" " * liczba_spacji, end="")
        print("*" * liczba_gwiazdek)


# Pobranie wysokości od użytkownika
wysokosc = int(input("Podaj wysokość trójkąta: "))

# Rysowanie trójkąta z odbiciem
rysuj_trojkat_z_odbiciem(wysokosc)
