import math
from datetime import datetime

# A)
def biometer_couter(t):

    psychical = math.sin((2 * math.pi / 23) * t)
    emotional = math.sin((2 * math.pi / 28) * t)
    inteligents = math.sin((2 * math.pi / 33) * t)

    return psychical, emotional, inteligents

def life_days_counter(birthday):
    today = datetime.today()
    counter = today - birthday

    return counter.days

# B) 
def congratulates_function(bio_value, bio_value2):
    if bio_value > 0.5:
        return "Gratulacje dzisiaj jest twoj dzien!" 
    elif bio_value < -0.5:
        if bio_value > bio_value2:
            return "Nie martw sie jutro bedzie lepiej!" 
        else:
            return "Niestety musisz przezyc ten okres dasz rade!" 
    else:
        return "Czujesz sie normlanie to tez spoko!" 
    

def main():
    name = input("Podaj swoje imie: ")
    birth_year = int(input("Podaj rok urodzenia: "))
    birth_month = int(input("Podaj miesiac urodzenia: "))
    birth_day = int(input("Podaj dzien urodzenia: "))

    birthday = datetime(birth_year, birth_month, birth_day)

    day_counter = life_days_counter(birthday)

    day_counter2 = life_days_counter(birthday) + 1

    psychical, emotional, inteligence = biometer_couter(day_counter)
    psychical2, emotional2, inteligence2 = biometer_couter(day_counter2)

    print(f"\nCzesc {name} dzisiaj jest twoj {day_counter} dzien zycia!")
    
    print(f"Twoje dzisiejsze parametry biometryczne wygladaja nastepujaco:")
    
    print(f"Fizyczny: {psychical:.2f} {congratulates_function(psychical, psychical2)}")
    print(f"Emocjonalny: {emotional:.2f} {congratulates_function(emotional, emotional2)}") 
    print(f"Intelektualny: {inteligence:.2f} {congratulates_function(inteligence, inteligence2)}")

if __name__ == "__main__":
    main()

# c)
# Lacznie na pisanie podpunktu a-b zajelo mi to jakies 30-40 minut
