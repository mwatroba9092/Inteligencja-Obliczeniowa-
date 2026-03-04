import math
import random
import matplotlib.pyplot as plt
import numpy as np

def symulacja_trebusza():
    # Ustalenie stałych parametrów
    v0 = 50.0  # początkowa prędkość w m/s
    h = 100.0  # początkowa wysokość w m
    g = 9.81   # przyspieszenie ziemskie w m/s^2

    # 1. Losowanie celu w odległości [50, 340]
    cel = random.randint(50, 340)
    print(f"Cel do zniszczenia znajduje się w odległości: {cel} metrów.")
    print(f"Margines błędu to 5 metrów (musisz trafić w przedział [{cel-5}, {cel+5}]).")
    
    proby = 0

    # 2. Pętla while dająca kolejne szanse
    while True:
        proby += 1
        
        # Pobranie kąta od użytkownika
        try:
            kat_stopnie = float(input("\nPodaj kąt strzału w stopniach (α): "))
        except ValueError:
            print("To nie jest prawidłowa liczba. Spróbuj ponownie.")
            continue

        # Zamiana stopni na radiany
        kat_radiany = math.radians(kat_stopnie)

        # Obliczanie odległości
        czesc_1 = v0 * math.sin(kat_radiany)
        czesc_pod_pierwiastkiem = (v0**2) * (math.sin(kat_radiany)**2) + 2 * g * h
        czesc_2 = math.sqrt(czesc_pod_pierwiastkiem)
        czesc_3 = (v0 * math.cos(kat_radiany)) / g
        
        dystans = (czesc_1 + czesc_2) * czesc_3

        print(f"Twój pocisk poleciał na odległość: {dystans:.2f} m.")

        # Sprawdzenie, czy pocisk trafił w cel (margines +- 5 metrów)
        if abs(dystans - cel) <= 5:
            print(f"Cel trafiony! Całkowita liczba Twoich prób: {proby}")
            
            # --- Generowanie i zapisywanie wykresu trajektorii ---
            
            # 1. Tworzenie punktów dla wykresu
            x_values = np.linspace(0, dystans, 1000) # 1000 punktów od startu do uderzenia
            tan_a = math.tan(kat_radiany)
            
            # Wzór na trajektorię
            y_values = (-g / (2 * (v0 * math.cos(kat_radiany))**2)) * x_values**2 + (tan_a) * x_values + h
            
            # 2. Konfiguracja wykresu
            fig, ax = plt.subplots(figsize=(10, 6))
            
            # Rysowanie głównej linii trajektorii
            ax.plot(x_values, y_values, color='tab:blue')
            
            # Ustawienia tytułu i etykiet osi
            ax.set_title('Trajektoria pocisku')
            ax.set_xlabel('Dystans [m]')
            ax.set_ylabel('Wysokość [m]')
            
            # Włączenie siatki i ustawienie jej typu
            ax.grid(True)
            
            # Ustawienie limitów osi (żeby wykres wyglądał ładniej przy upadku na ziemię)
            ax.set_ylim(bottom=-10, top=max(y_values) + 10)
            
            # 3. Zapisanie wykresu do pliku
            nazwa_pliku = f'trajektoria_trafienie_{proby}.png'
            plt.savefig(nazwa_pliku)
            print(f"Wygenerowano wykres trajektorii i zapisano go do pliku: {nazwa_pliku}")
            
            # 4. Zamknięcie wykresu z pamięci
            plt.close(fig)
            
            break # Zakończenie pętli po trafieniu
        else:
            print("Pudło! Spróbuj dobrać inny kąt.")

# Uruchomienie programu
if __name__ == "__main__":
    symulacja_trebusza()