import math
from datetime import datetime

# A) Obliczenia biorytmu
def calculate_biorythms(t):
    """Oblicza wartości biorytmów dla danego dnia życia."""
    # Wykorzystanie LaTeX do wzoru: $$ \sin\left(\frac{2\pi}{P} \cdot t\right) $$
    physical = math.sin((2 * math.pi / 23) * t)
    emotional = math.sin((2 * math.pi / 28) * t)
    intellectual = math.sin((2 * math.pi / 33) * t)

    return physical, emotional, intellectual

def get_days_lived(birthday):
    """Oblicza liczbę przeżytych dni."""
    today = datetime.today()
    delta = today - birthday
    return delta.days

# B) Funkcja logiczna z poprawioną stylistyką
def get_feedback(current_val, next_val):
    """Zwraca komentarz na podstawie dzisiejszego wyniku i trendu na jutro."""
    if current_val > 0.5:
        return "Gratulacje, dzisiaj jest Twój dzień!" 
    elif current_val < -0.5:
        if next_val > current_val:
            return "Nie martw się, jutro będzie lepiej!" 
        else:
            return "Niestety musisz przetrwać ten słabszy okres, dasz radę!" 
    else:
        return "Czujesz się normalnie – to też spoko!" 

def main():
    print("--- Kalkulator Biorytmów ---")
    name = input("Podaj swoje imię: ")
    
    try:
        birth_year = int(input("Podaj rok urodzenia (np. 1995): "))
        birth_month = int(input("Podaj miesiąc urodzenia (1-12): "))
        birth_day = int(input("Podaj dzień urodzenia: "))
        birthday = datetime(birth_year, birth_month, birth_day)
    except ValueError:
        print("Błąd: Podano nieprawidłową datę!")
        return

    # Obliczenia dla dzisiaj i jutra
    days_today = get_days_lived(birthday)
    days_tomorrow = days_today + 1

    # Pobranie wyników
    p1, e1, i1 = calculate_biorythms(days_today)
    p2, e2, i2 = calculate_biorythms(days_tomorrow)

    # Wyświetlanie wyników
    print(f"\nCześć {name}! Dzisiaj jest Twój {days_today}. dzień życia.")
    print("-" * 30)
    print(f"Fizyczny:     {p1:6.2f} | {get_feedback(p1, p2)}")
    print(f"Emocjonalny:  {e1:6.2f} | {get_feedback(e1, e2)}") 
    print(f"Intelektualny: {i1:6.2f} | {get_feedback(i1, i2)}")
    print("-" * 30)

if __name__ == "__main__":
    main()

# D)
#WERSJA POPRAWIONA PRZEZ AI