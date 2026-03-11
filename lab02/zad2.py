import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

df = pd.read_csv('iris_big.csv')

X = df.drop('target_name', axis=1)
y = df['target_name']
print("Oto kilka pierwszych wierszy naszych oryginalnych danych z pliku:")
print(X.head())

pca_full = PCA(n_components=4).fit(X)

variances = pca_full.explained_variance_
print("\nWariancje poszczególnych składowych PCA (dla wszystkich 4 osi):")
print(variances)

strata_2_kolumny = sum(variances[2:]) / sum(variances)
print(f"Strata informacji po usunięciu 2 kolumn: {strata_2_kolumny:.2%}")

strata_3_kolumny = sum(variances[1:]) / sum(variances)
print(f"Strata informacji po usunięciu 3 kolumn: {strata_3_kolumny:.2%}")

pca_iris = PCA(n_components=2).fit(X)
print("\nMacierz komponentów PCA dla oryginalnych danych:")
print(pca_iris.components_)

transformed_iris = pca_iris.transform(X)
pca = pd.DataFrame(transformed_iris, columns=['PCA1', 'PCA2'])

# Wariancje wykazała, że dla dwóch pierwszych składowych zachowujemy 97.77% wariancji, co jest większe niż 95%.
# Dlatego można usunąć dwie kolumny, tak aby zachować minimum 95% wariancji.

pca['FlowerType'] = y.values

plt.figure(figsize=(8, 6))

gatunki = pca['FlowerType'].unique()
kolory = ['#440154', '#21918c', '#fde725'] 

for gatunek, kolor in zip(gatunki, kolory):
    subset = pca[pca['FlowerType'] == gatunek]
    plt.scatter(subset['PCA1'], subset['PCA2'], c=kolor, label=gatunek)

plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.title('PCA zbioru danych iris_big.csv')
plt.legend()
plt.savefig('PCA.png')
print("\nWykres został poprawnie wygenerowany i zapisany jako PCA.png!")
