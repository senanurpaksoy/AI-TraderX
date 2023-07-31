import yfinance as yf
import datetime as dt


def get_stock_market_data_basic(stockmarket_symbol, startDate, endDate):

    stock_data = yf.download(stockmarket_symbol, start=startDate, end=endDate)
    return stock_data
# Bugun için  sonuçların verildiği fonksiyn
today = dt.date.today()
def get_stock_market_data_basic_today(stockmarket_symbol, startDate):

    stock_data = yf.download(stockmarket_symbol, start=startDate, end=today)
    return stock_data


# Borsa marketimize ait temel bilgileri çıktı olarak verir.
def get_stock_market_data_get_info(stockmarket):

    stockMarketData = yf.Ticker(f"{stockmarket}")

    # display Company Sector
    print("Company Sector : ", stockMarketData.info["sector"])

    # display Price Earnings Ratio
    print("Price Earnings Ratio : ", stockMarketData.info["trailingPE"])

    # display Company Beta
    print(" Company Beta : ", stockMarketData.info["beta"])
    # Hisse senedi fiyatları
    print(" Company Close Value : ", stockMarketData.info["Close"])


def get_stock_market_data_get_info_today(stockmarket):

    stockMarketData = yf.Ticker(f"{stockmarket}")

    # display Company Sector
    print("Company Sector : ", stockMarketData.info["sector"])

    # display Price Earnings Ratio
    print("Price Earnings Ratio : ", stockMarketData.info["trailingPE"])

    # display Company Beta
    print(" Company Beta : ", stockMarketData.info["beta"])
    # Hisse senedi fiyatları
    print(" Company Close Value : ", stockMarketData.info["Close"])
