import pandas as pd
import difflib
import re

def correct_species_name(name, correct_species):
    name = str(name).strip().lower()
    if name in correct_species:
        return name
    else:
        correct_name = difflib.get_close_matches(name, correct_species, n=1, cutoff=0.6)
        if correct_name:
            return correct_name[0]
        else:
            print(f'Cannot find correct species for: {name}')
            return name

# A)
cleaned_lines = []
with open('iris_big_with_errors.csv', 'r', encoding='utf-8') as f:
    for line in f:
        fixed_line = re.sub(r'(\d),(\d)', r'\1.\2', line)
        cleaned_lines.append(fixed_line)

with open('iris_fixed_structure.csv', 'w', encoding='utf-8') as f:
    f.writelines(cleaned_lines)

df = pd.read_csv('iris_fixed_structure.csv')

numeric_columns = ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors='coerce')

# B)
print("\n--- Brakujące dane ---")
empty_data = df.isna().sum() + (df == ' ').sum() + (df == '-').sum()
print(empty_data)

print("\n--- Statystyki bazy danych z błędami ---")

print(df.describe(include='all'))


# C)
for column in numeric_columns:
    median = df[column].median()
    invalid_data = (df[column] <= 0) | (df[column] >= 15) | df[column].isna() | (df[column] == ' ') | (df[column] == '-')
    df.loc[invalid_data, column] = median

print("\nThe numeric data has been corrected.")


# C (D) )
species = df['target_name'].unique()
correct_species = ['setosa', 'versicolor', 'virginica']

print("\n--- Sprawdzanie gatunków ---")
if len(species) == 3 and all(s in correct_species for s in species):
    print("All species are correct")
else:
    print("There are some errors in species column")
    print(f'There are {len(species)} species in the dataset')
    print(f'Current species in file:\n{species}\n')

    df['target_name'] = df['target_name'].apply(lambda x: correct_species_name(x, correct_species))

    najczestszy_gatunek = df['target_name'].mode()[0]
    df['target_name'] = df['target_name'].replace(['unknown', 'nan'], najczestszy_gatunek)
    
    print(f'\nCorrected species in file: {df["target_name"].unique()}')

df.to_csv('iris_corrected.csv', index=False)
print("\nThe completely corrected data has been saved to iris_corrected.csv")