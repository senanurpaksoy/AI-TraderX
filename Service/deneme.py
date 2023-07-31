import yfinance as yf
import pandas as pd

# Hisse senedi sembolü
stock_symbol = "AAPL"

# Veri aralığı
start_date = "2023-01-01"
end_date = "2023-07-31"

# Veri çekme
stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

# Hisse senedi fiyatları
stock_prices = stock_data["Close"]

# Hisse senedi işlem hacmi
stock_volume = stock_data["Volume"]

# Teknik göstergeler
# Hareketli Ortalama (Moving Average)
stock_data["MA_20"] = stock_data["Close"].rolling(window=20).mean()
stock_data["MA_50"] = stock_data["Close"].rolling(window=50).mean()

# Göreceli Güç Endeksi (Relative Strength Index - RSI)
delta = stock_data["Close"].diff(1)
gain = delta.where(delta > 0, 0)
loss = -delta.where(delta < 0, 0)

avg_gain = gain.rolling(window=14).mean()
avg_loss = loss.rolling(window=14).mean()

rs = avg_gain / avg_loss
rsi = 100 - (100 / (1 + rs))
stock_data["RSI"] = rsi

# Verileri görselleştirme
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))
plt.plot(stock_data.index, stock_data["Close"], label="Kapanış Fiyatı", color="blue")
plt.plot(stock_data.index, stock_data["MA_20"], label="20 Günlük Ortalama", color="orange")
plt.plot(stock_data.index, stock_data["MA_50"], label="50 Günlük Ortalama", color="green")
plt.plot(stock_data.index, stock_data["RSI"], label="RSI", color="purple")
plt.legend()
plt.title("AAPL Hisse Senedi Fiyatları ve Hareketli Ortalamalar")
plt.xlabel("Tarih")
plt.ylabel("Fiyat")
plt.show()