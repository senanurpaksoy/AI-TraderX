import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# İki örnek matrisi oluşturalım
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[9, 8, 7],
                    [6, 5, 4],
                    [3, 2, 1]])

# Korelasyon matrisini hesaplayalım
correlation_matrix = np.corrcoef(matrix1.ravel(), matrix2.ravel())

print("Korelasyon Matrisi:")
print(correlation_matrix)

# Korelasyon matrisini ısı haritası olarak görselleştirme
plt.figure(figsize=(6, 4))
plt.imshow(correlation_matrix, cmap='coolwarm', vmin=-1, vmax=1)
plt.colorbar(label='Korelasyon Değeri')
plt.title('Matrisler Arasındaki Korelasyon')
plt.xticks([0, 1], ['Matrix 1', 'Matrix 2'])
plt.yticks([0, 1], ['Matrix 1', 'Matrix 2'])
plt.show()
