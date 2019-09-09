# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


class profit:
    __metaclass__ = ABCMeta

    def __init__(self, profit_evaluator=None):
        self.__profit_evaluator = profit_evaluator

    def other_profit_evaluator(self, wallet):
        if self.__profit_evaluator is None:
            return 0
        return self.__profit_evaluator.evaluate(wallet)

    @abstractmethod
    def evaluate(self, wallet):
        pass


def special_profit(function_or_method):
    def wrapper(self, wallet):
        return function_or_method(self, wallet) + 1.0
    return wrapper


class template_evaluate(profit):
    __metaclass__ = ABCMeta

    def evaluate(self, wallet):
        if self.special_offer(wallet):
            return self.max_evaluate(wallet) + self.other_profit_evaluator(wallet)
        else:
            return self.min_evaluate(wallet) + self.other_profit_evaluator(wallet)

    @abstractmethod
    def special_offer(self, wallet):
        pass

    @abstractmethod
    def max_evaluate(self, wallet):
        pass

    @abstractmethod
    def min_evaluate(self, wallet):
        pass


class twenty_percent(template_evaluate):

    def special_offer(self, wallet):
        if wallet.amount > 1000:
            return True
        else:
            return False

    def max_evaluate(self, wallet):
        return wallet.amount * 0.25

    def min_evaluate(self, wallet):
        return wallet.amount * 0.20


class ten_percent(template_evaluate):

    def special_offer(self, wallet):
        if wallet.stocks >= 3:
            return True
        else:
            return False

    def max_evaluate(self, wallet):
        return wallet.amount * 0.12

    def min_evaluate(self, wallet):
        return wallet.amount * 0.10


class five_percent(profit):

    def evaluate(self, wallet):
        return wallet.amount * 0.05 + self.other_profit_evaluator(wallet)


class two_percent(profit):

    @special_profit
    def evaluate(self, wallet):
        return wallet.amount * 0.02 + self.other_profit_evaluator(wallet)
