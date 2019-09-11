# -*- coding: UTF-8 -*-
from datetime import date


if __name__ == "__main__":

    from observer import printing, saving, sending
    from stock import Stock, Wallet

    stocks = [
        Stock("Google", 60),
        Stock("Microsoft", 10),
        Stock("Apple", 20),
        Stock("Github", 10)
    ]

    observers = [printing, sending, saving]

    wallet = Wallet(
        "John Doe",
        "126549871-5",
        stocks,
        observers=observers
    )
