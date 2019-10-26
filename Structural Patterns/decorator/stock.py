# -*- coding: UTF-8 -*-
class Wallet:

    def __init__(self):
        self.__stocks = []

    @property
    def amount(self):
        amount = 0.0
        for stock in self.__stocks:
            amount += stock.value
        return amount

    @property
    def stocks(self):
        return len(self.__stocks)

    def get_stocks(self):
        return tuple(self.__stocks)

    def append_stock(self, stock):
        self.__stocks.append(stock)


class Stock:
    def __init__(self, name, value):
        self.__name = value
        self.__value = value

    @property
    def name(self):
        return self.__name

    @property
    def value(self):
        return self.__value
