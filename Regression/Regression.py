from sklearn.ensemble import RandomForestRegressor
import Data.Stockdata as sd
import datetime
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.svm import SVR
'''import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense'''
import numpy as np
import yfinance as yf

stock_data = sd.get_stock_market_data_basic_today("AAPL","2010-01-01")


def RandomForestRegressPredict(stock_symbol,forecast_steps_input,end_date,start_date):
    stock_data = sd.get_stock_market_data_basic(stock_symbol,start_date,end_date)

    # Hisse senedi kapanış fiyatları
    stock_prices = stock_data["Close"]

    # Özellik ve hedef değişken oluşturma
    X = stock_prices[:-1].values.reshape(-1, 1)  # Önceki fiyatları kullanarak tahmin yapacağız
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

def svr_predict(data):
    svr = SVR()
    svr.fit(np.arange(len(data)).reshape(-1, 1), data)
    return svr.predict([[len(data)]])[0]


'''
def neural_network_predict(data):
    model = Sequential()
    model.add(Dense(8, input_dim=1, activation='relu'))
    model.add(Dense(1))
    model.compile(loss='mean_squared_error', optimizer='adam')
    model.fit(np.arange(len(data)).reshape(-1, 1), data, epochs=100, batch_size=1, verbose=0)
    return model.predict([[len(data)]])[0][0]

'''


def get_stock_data(symbol, start_date, end_date):
    data = yf.download(symbol, start=start_date, end=end_date)
    return data['Close']

aapl_data = get_stock_data('AAPL', '2023-01-01', '2023-07-31')

# Veriyi ve algoritma tahminlerini görselleştirme
plt.figure(figsize=(10, 6))
plt.plot(aapl_data.index, aapl_data, label='AAPL Close Prices', color='blue')
plt.axvline(x=aapl_data.index[-1], color='red', linestyle='--', label='Prediction Date')


linear_regression_result = linear_regression_predict(aapl_data)
decision_tree_result = decision_tree_predict(aapl_data)
random_forest_result = random_forest_predict(aapl_data)
svr_result = svr_predict(aapl_data)


# Algoritmaların tahminleri
plt.scatter(aapl_data.index[-1], linear_regression_result, color='green', marker='o', label='Linear Regression')
plt.scatter(aapl_data.index[-1], decision_tree_result, color='orange', marker='o', label='Decision Tree')
plt.scatter(aapl_data.index[-1], random_forest_result, color='purple', marker='o', label='Random Forest')
plt.scatter(aapl_data.index[-1], svr_result, color='magenta', marker='o', label='SVR')

plt.xlabel('Date')
plt.ylabel('Price')
plt.title('AAPL Stock Price Prediction')
plt.legend()
plt.grid(True)
plt.show()

print("Linear Regression Result:", linear_regression_result)
print("Decision Tree Result:", decision_tree_result)
print("Random Forest Result:", random_forest_result)
print("SVR Result:", svr_result)
print("Neural Network Result:", neural_network_result)





