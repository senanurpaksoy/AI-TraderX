from sklearn.ensemble import RandomForestRegressor
import Data.Stockdata as sd
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
import yfinance as yf



stock_data = sd.get_stock_market_data_basic_today("AAPL", "2010-01-01")


def RandomForestRegressPredict(
    stock_symbol, forecast_steps_input, end_date, start_date
):
    stock_data = sd.get_stock_market_data_basic(stock_symbol, start_date, end_date)

    # Hisse senedi kapanış fiyatları
    stock_prices = stock_data["Close"]

    # Özellik ve hedef değişken oluşturma
    X = stock_prices[:-1].values.reshape(
        -1, 1
    )  # Önceki fiyatları kullanarak tahmin yapacağız
    y = stock_prices[1:].values  # Bir sonraki günün fiyatları tahmin edilecek

    # Model oluşturma ve eğitme
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    # İleriye dönük tahmin için adım sayısı
    forecast_steps = forecast_steps_input

    # Tahmin yapma
    last_price = X[-1][0]
    forecast = []
    for _ in range(forecast_steps):
        next_price = model.predict([[last_price]])
        forecast.append(next_price[0])
        last_price = next_price[0]

    return forecast[-1]


def linear_regression_predict(data):
    lr = LinearRegression()
    lr.fit(np.arange(len(data)).reshape(-1, 1), data)
    return lr.predict([[len(data)]])[0]


def decision_tree_predict(data):
    dt = DecisionTreeRegressor()
    dt.fit(np.arange(len(data)).reshape(-1, 1), data)
    return dt.predict([[len(data)]])[0]


def random_forest_predict(data):
    rf = RandomForestRegressor()
    rf.fit(np.arange(len(data)).reshape(-1, 1), data)
    return rf.predict([[len(data)]])[0]


def polynomial_regression_predict(data):
    # Polinom Regresyon için derecesi 2 olan bir polinom modeli kullanalım.
    poly_features = np.polyfit(np.arange(len(data)), data, 2)
    poly_reg = np.poly1d(poly_features)
    return poly_reg(len(data))


def svr_predict(data):
    svr = SVR()
    svr.fit(np.arange(len(data)).reshape(-1, 1), data)
    return svr.predict([[len(data)]])[0]


def logistic_regression_predict(data):
    x = np.arange(len(data)).reshape(-1, 1)
    y = (data.shift(-1) > data).astype(
        int
    )  # Binary classification (1 if next day price increase, 0 otherwise)

    lr = LogisticRegression()
    lr.fit(x, y)
    return lr.predict([[len(data)]])[0]


def neural_network_predict(data):
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation="relu"))
    model.add(Dense(1))
    model.compile(loss="mean_squared_error", optimizer="adam")
    model.fit(
        np.arange(len(data)).reshape(-1, 1), data, epochs=100, batch_size=1, verbose=0
    )
    return model.predict([[len(data)]])[0][0]


def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data["Close"]


aapl_data = sd.get_stock_market_data_basic("AAPL", "2023-01-01", "2023-07-31")
