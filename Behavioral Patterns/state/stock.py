# -*- coding: UTF-8 -*-

from abc import ABCMeta, abstractmethod


class State:

    __metaclass__ = ABCMeta

    def __init__(self):
        self.extra_profit_applied = False

    @abstractmethod
    def apply_extra_profit(self, wallet):
        pass

    @abstractmethod
    def approve(self, wallet):
        pass

    @abstractmethod
    def deny(self, wallet):
        pass

    @abstractmethod
    def terminate(self, wallet):
        pass


class OnHold(State):
    def apply_extra_profit(self, wallet):
        if not self.extra_profit_applied:
            wallet.add_extra_profit(wallet.amount * 0.01)
            self.extra_profit_applied = True
        else:
            raise Exception('Extra profit already applied!')

    def approve(self, wallet):
        wallet.state = Approved()

    def deny(self, wallet):
        wallet.state = Denied()

    def terminate(self, wallet):
        raise Exception("Wallet ON HOLD cannot be TERMINATED")


class Approved(State):
    def apply_extra_profit(self, wallet):
        if not self.extra_profit_applied:
            wallet.add_extra_profit(wallet.amount * 0.05)
            self.extra_profit_applied = True
        else:
            raise Exception('Extra profit already applied!')

    def approve(self, wallet):
        raise Exception("Wallet is already APPROVED")

    def deny(self, wallet):
        raise Exception("Wallet is already APPROVED cannot be DENIED")

    def terminate(self, wallet):
        wallet.state = Terminate()


class Denied(State):
    def apply_extra_profit(self, wallet):
        raise Exception(
            "Wallet DENIED!. Impossible to evaluate extra profit.")

    def approve(self, wallet):
        raise Exception("Wallet is already DENIED cannot be APPROVED")

    def deny(self, wallet):
        raise Exception("Wallet is already DENIED")

    def terminate(self, wallet):
        wallet.state = Terminate()


class Terminate(State):
    def apply_extra_profit(self, wallet):
        raise Exception(
            "Wallet TERMINATE! Impossible to evaluate extra profit.")

    def approve(self, wallet):
        raise Exception("Wallet is already TERMINATED cannot be APPROVED")

    def deny(self, wallet):
        raise Exception("Wallet is already TERMINATED cannot be DENIED")

    def terminate(self, wallet):
        raise Exception("Wallet is already TERMINATED")


class Wallet:

    def __init__(self):
        self.__stocks = []
        self.state = OnHold()
        self.__extra_profit = 0

    def apply_extra_profit(self):
        self.state.apply_extra_profit(self)

    def approve(self):
        self.state.approve(self)

    def deny(self):
        self.state.deny(self)

    def terminate(self):
        self.state.terminate(self)

    @property
    def amount(self):
        amount = 0.0
        for stock in self.__stocks:
            amount += stock.value
        return amount + self.__extra_profit

    @property
    def stocks(self):
        return len(self.__stocks)

    def get_stocks(self):
        return tuple(self.__stocks)

    def append_stock(self, stock):
        self.__stocks.append(stock)

    def add_extra_profit(self, extra_profit):
        self.__extra_profit = extra_profit


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
