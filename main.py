
from Service import Stockdata


def main():
    print("Hello World")



if __name__ == '__main__':
    start_date = "2023-01-01"
    end_date = "2023-07-31"
    Stockdata.get_stock_market("AAPL",startDate=start_date,endDate=end_date)
