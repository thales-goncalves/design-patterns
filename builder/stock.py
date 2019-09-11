# -*- coding: UTF-8 -*-
from datetime import date


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


class Wallet:

    def __init__(self, owner, ss_number, stocks, date=date.today(), description=''):
        self.__owner = owner
        self.__ss_number = ss_number
        self.__date = date
        if len(description) > 20:
            raise Exception("Description cannot have more than 20 characters!")
        self.__description = description
        self.__stocks = stocks

    def get_stocks(self):
        return tuple(self.__stocks)

    @property
    def amount(self):
        amount = 0.0
        for stock in self.__stocks:
            amount += stock.value
        return amount

    @property
    def stocks_len(self):
        return len(self.__stocks)

    @property
    def owner(self):
        return self.__owner

    @property
    def ss_number(self):
        return self.__ss_number

    @property
    def date(self):
        return self.__date

    @property
    def description(self):
        return self.__description

    @property
    def stocks(self):
        return self.__stocks
