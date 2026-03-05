import pandas as pd
import difflib

def correct_species_name(name, correct_species):
    name = str(name).strip().lower()
    if name in correct_species:
        return name
    else:
        correct_name = difflib.get_close_matches(name, correct_species, n=1, cutoff=0.5)
        if correct_name:
            return correct_name[0]
        else:
            print(f'Nie można znaleźć poprawnego dopasowania dla gatunku: {name}')
            return name


df = pd.read_csv('iris_big_with_errors.csv', on_bad_lines='skip')

print(df.shape)
print(df.info())

empty_data = df.isna().sum() + (df == ' ').sum() + (df == '-').sum()
print("Brakujące lub nieuzupełnione dane:")
print(empty_data)

print("\nStatystyki bazy danych z błędami:")
print(df.describe(include='all'))

numeric_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']
for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

for column in numeric_columns:
    median = df[column].median()
    invalid_data = (df[column] <= 0) | (df[column] >= 15) | df[column].isna()
    df.loc[invalid_data, column] = median

species = df['target_name'].unique()
correct_species = ['setosa', 'versicolor', 'virginica']

print("\n--- Sprawdzanie gatunków ---")
if len(species) == 3 and all(s in correct_species for s in species):
    print("Wszystkie nazwy gatunków są poprawne.")
else:
    print("Wykryto błędy w kolumnie z nazwami gatunków.")
    print(f'Liczba unikalnych wartości w kolumnie gatunków: {len(species)}')
    print(f'Obecne wartości w pliku: {species}')

    df['target_name'] = df['target_name'].apply(lambda x: correct_species_name(x, correct_species))
    print(f'Poprawione gatunki w pliku: {df["target_name"].unique()}')

df.to_csv('iris_corrected.csv', index=False)
print("\nDane zostały poprawione i zapisane do pliku iris_corrected.csv")