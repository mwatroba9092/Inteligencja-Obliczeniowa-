import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler, StandardScaler

def data_plot(df, ax, title):
    for species in df['target_name'].unique():
        data = df[df['target_name'] == species]
        ax.scatter(data['sepal length (cm)'], data['sepal width (cm)'], label=species, s=20)
    
    ax.set_title(title, fontsize=10)
    ax.set_xlabel('Sepal Length (cm)')
    ax.set_ylabel('Sepal Width (cm)')
    ax.legend()

df = pd.read_csv('iris_corrected.csv')

fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 6))

# 1. Dane oryginalne (Lewy)
data_plot(df, ax1, 'Original Dataset')

# 2. Zeskalowane z-scorem (Środkowy)
scaler_zscore = StandardScaler()
X_zscore = scaler_zscore.fit_transform(df[['sepal length (cm)', 'sepal width (cm)']])
df_zscore = pd.DataFrame(X_zscore, columns=['sepal length (cm)', 'sepal width (cm)'])
df_zscore['target_name'] = df['target_name']
data_plot(df_zscore, ax2, 'Z-Score Scaled Dataset')

# 3. Znormalizowane min-max (Prawy)
scaler_minmax = MinMaxScaler()
X_minmax = scaler_minmax.fit_transform(df[['sepal length (cm)', 'sepal width (cm)']])
df_minmax = pd.DataFrame(X_minmax, columns=['sepal length (cm)', 'sepal width (cm)'])
df_minmax['target_name'] = df['target_name']
data_plot(df_minmax, ax3, 'Min-Max Normalised Dataset')

plt.tight_layout() 
plt.savefig('iris_plot.png')
plt.show()