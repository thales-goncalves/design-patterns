# -*- coding: UTF-8 -*-
from datetime import date
from stock import Wallet


class Stock_Builder:

    def __init__(self):
        self.__owner = None
        self.__ss_number = None
        self.__date = None
        self.__description = None
        self.__stocks = None

    def with_owner(self, owner):
        self.__owner = owner
        return self

    def with_ss_number(self, ss_number):
        self.__ss_number = ss_number
        return self

    def with_stocks(self, stocks):
        self.__stocks = stocks
        return self

    def with_date(self, date):
        self.__date = date
        return self

    def with_description(self, description):
        self.__description = description
        return self

    def build(self):
        if self.__owner is None:
            raise Exception("Owner is mandatory")
        if self.__ss_number is None:
            raise Exception("Social Security Number is mandatory")
        if self.__stocks is None:
            raise Exception("No stocks founded")
        if self.__date is None:
            self.__date = date.today()
        if self.__description is None:
            self.__description = ""

        return Wallet(
            owner=self.__owner,
            ss_number=self.__ss_number,
            stocks=self.__stocks,
            date=self.__date,
            description=self.__description
        )
