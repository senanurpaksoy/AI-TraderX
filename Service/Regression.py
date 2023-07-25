import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import matplotlib.pyplot as plt

# Hisse senedi sembolü
stock_symbol = "AAPL"

# Veri aralığı
start_date = "2010-01-01"
end_date = "2023-07-31"

# Veri çekme
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Hisse senedi kapanış fiyatları
stock_prices = stock_data["Close"]

# Özellik ve hedef değişken oluşturma
X = stock_prices[:-1].values.reshape(-1, 1)  # Önceki fiyatları kullanarak tahmin yapacağız
y = stock_prices[1:].values  # Bir sonraki günün fiyatları tahmin edilecek

# Model oluşturma ve eğitme
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# İleriye dönük tahmin için adım sayısı
forecast_steps = 20

# Tahmin yapma
last_price = X[-1][0]
forecast = []
for _ in range(forecast_steps):
    next_price = model.predict([[last_price]])
    forecast.append(next_price[0])
    last_price = next_price[0]

# Son tahmin edilen fiyatı ekrana yazdırma
print("Son tahmin edilen fiyat:", forecast[-1])

# Sonuçları görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(stock_prices, label="Gerçek Fiyatlar", color="blue")
plt.plot(range(len(stock_prices), len(stock_prices) + forecast_steps), forecast, label="Tahmin Edilen Fiyatlar", color="orange")
plt.scatter(len(stock_prices) + forecast_steps - 1, forecast[-1], color='red', marker='x', label='Son Tahmin')
plt.legend()
plt.title("AAPL Hisse Senedi Fiyat Tahmini (Random Forests)")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.xticks(rotation=45)
plt.show()
