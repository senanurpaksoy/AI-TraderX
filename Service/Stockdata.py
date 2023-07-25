import yfinance as yahooFinance


def get_stock_market(stockmarket):

    stockMarketData = yahooFinance.Ticker(f"{stockmarket}")

        # display Company Sector
    print("Company Sector : ", stockMarketData.info['sector'])

        # display Price Earnings Ratio
    print("Price Earnings Ratio : ", stockMarketData.info['trailingPE'])

        # display Company Beta
    print(" Company Beta : ", stockMarketData.info['beta'])




