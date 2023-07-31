import yfinance as yahooFinance


def get_stock_market_data_basic(stockmarket,startDate,endDate):

    stockMarketData = yahooFinance.Ticker(f"{stockmarket}")

        # display Company Sector
    print("Company Sector : ", stockMarketData.info['sector'])

        # display Price Earnings Ratio
    print("Price Earnings Ratio : ", stockMarketData.info['trailingPE'])

        # display Company Beta
    print(" Company Beta : ", stockMarketData.info['beta'])
    # Hisse senedi fiyatları
    print(" Company Close Value : ", stockMarketData.info['Close'])


def get_stock_market_data_basic(stockmarket,startDate,endDate):

    stockMarketData = yahooFinance.Ticker(f"{stockmarket}")

        # display Company Sector
    print("Company Sector : ", stockMarketData.info['sector'])

        # display Price Earnings Ratio
    print("Price Earnings Ratio : ", stockMarketData.info['trailingPE'])

        # display Company Beta
    print(" Company Beta : ", stockMarketData.info['beta'])
    # Hisse senedi fiyatları
    print(" Company Close Value : ", stockMarketData.info['Close'])
