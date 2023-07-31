import yfinance as yf
import pandas as pd
import datetime
import Data.Stockdata as sd


# Hisse senedi sembolü
stock_symbol = "AAPL"

# Veri aralığı
start_date = "2023-01-01"


print()
# Veri çekme
stock_data = sd.get_stock_market_data_basic_today(stock_symbol, start_date)

# Hisse senedi fiyatları
stock_prices = stock_data["Close"]

# Hisse senedi işlem hacmi
stock_volume = stock_data["Volume"]


# Kişilerin girdikleri inputa göre hareketli ortalama alacakları fonksiyon
def Moving_average(stock_symbol, day_time):
    # Teknik göstergeler
    # Hareketli Ortalama (Moving Average)
    stock_data["MA_20"] = stock_data["Close"].rolling(window=day_time).mean()
    return stock_data[f"MA_{day_time}"]


#  20 günlük hareketli ortalama için
def Moving_average_20(stock_symbol):

    stock_data = sd.get_stock_market_data_basic_today(stock_symbol, start_date)
    # Teknik göstergeler
    # Hareketli Ortalama (Moving Average)
    stock_data["MA_20"] = stock_data["Close"].rolling(window=20).mean()
    return stock_data["MA_20"]


#  50 günlük hareketli ortalama için
def Moving_average_50(stock_symbol):
    # Teknik göstergeler
    # Hareketli Ortalama (Moving Average)
    stock_data["MA_20"] = stock_data["Close"].rolling(window=20).mean()
    return stock_data["MA_20"]


# Göreceli Güç Endeksi (Relative Strength Index - RSI)
def RSI(stock_symbol):
    stock_data = sd.get_stock_market_data_basic_today(stock_symbol, start_date)
    delta = stock_data["Close"].diff(1)
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    stock_data["RSI"] = rsi
    return stock_data["RSI"]

