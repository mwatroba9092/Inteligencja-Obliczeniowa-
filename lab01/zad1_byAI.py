import datetime
import math

def oblicz_biorytm(t, dlugosc_cyklu):
    """Oblicza wartość biorytmu dla danego dnia t i długości cyklu."""
    return math.sin((2 * math.pi * t) / dlugosc_cyklu)

def analizuj_wynik(wynik_dzis, wynik_jutro, nazwa_fali):
    """Sprawdza wynik i wypisuje odpowiedni komunikat według założeń punktu b."""
    print(f"\n--- Fala {nazwa_fali} ---")
    print(f"Twój dzisiejszy wynik: {wynik_dzis:.2f}")
    
    # Warunki dla wysokiego wyniku
    if wynik_dzis > 0.5:
        print("Gratulacje! Twój wynik jest wysoki. Ciesz się świetną formą!")
        
    # Warunki dla niskiego wyniku
    elif wynik_dzis < -0.5:
        print("Przykro mi, to słabszy moment. Dbaj o siebie i nie przemęczaj się dzisiaj.")
        # Sprawdzanie, czy jutro będzie lepiej
        if wynik_jutro > wynik_dzis:
            print("Nie martw się. Jutro będzie lepiej!")
        else:
            print("Jutro wskaźnik może jeszcze odrobinę spaść, ale pamiętaj - po każdym dołku jest odbicie w górę!")
            
    # Warunki dla wyniku neutralnego (pomiędzy -0.5 a 0.5)
    else:
        print("Twój wynik jest na średnim poziomie (faza przejściowa/neutralna).")

def main():
    print("=== KALKULATOR BIORYTMÓW ===")
    
    # KROK A: Pobieranie danych od użytkownika
    imie = input("Podaj swoje imię: ")
    
    try:
        rok = int(input("Podaj rok urodzenia (np. 1990): "))
        miesiac = int(input("Podaj miesiąc urodzenia (1-12): "))
        dzien = int(input("Podaj dzień urodzenia (1-31): "))
        
        data_urodzenia = datetime.date(rok, miesiac, dzien)
    except ValueError:
        print("Błąd! Wprowadź poprawną datę używając samych cyfr.")
        return

    dzisiaj = datetime.date.today()
    
    # Obliczanie przeżytych dni (t)
    roznica = dzisiaj - data_urodzenia
    t = roznica.days
    
    if t < 0:
        print("Hej, podróżniku w czasie! Podana data jest z przyszłości.")
        return

    print(f"\nCześć {imie}! Dzisiaj jest {t}. dzień Twojego życia.")

    # KROK B: Obliczenia i analiza z warunkami
    cykle = {
        "fizyczna": 23,
        "emocjonalna": 28,
        "intelektualna": 33
    }
    
    for nazwa, dlugosc in cykle.items():
        # Obliczamy wynik na dziś (t) i na jutro (t+1)
        dzis = oblicz_biorytm(t, dlugosc)
        jutro = oblicz_biorytm(t + 1, dlugosc)
        
        # Analizujemy i drukujemy wynik
        analizuj_wynik(dzis, jutro, nazwa)

    print("\n---------------------------------------------------")
    print("Pamiętaj: biorytmy to tylko ciekawa, pseudonaukowa koncepcja z początku XX wieku.")
    print("Jeśli czujesz się dzisiaj świetnie, a program mówi inaczej – ufaj sobie, nie matematyce!")

if __name__ == "__main__":
    main()