# -*- coding: UTF-8 -*-
from datetime import date
from pprint import pprint

if __name__ == "__main__":

    from stock import Stock, Wallet
    from stock_builder import Stock_Builder

    stocks = [
        Stock("Google", 60),
        Stock("Microsoft", 10),
        Stock("Apple", 20),
        Stock("Github", 10)
    ]

    wallet = Wallet(
        "John Doe",
        "126549871-5",
        stocks,
    )

    wallet_with_buidder = (Stock_Builder()
                           .with_owner("John Doe")
                           .with_ss_number("126549871-5")
                           .with_stocks(stocks)
                           .build())

    pprint(wallet_with_buidder.owner)
    pprint(wallet_with_buidder.ss_number)
    pprint(wallet_with_buidder.date)
