# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod


class template_evaluate:
    __metaclass__ = ABCMeta

    def evaluate(self, wallet):
        if self.special_offer(wallet):
            return self.max_evaluate(wallet)
        else:
            return self.min_evaluate(wallet)

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


class five_percent:

    def evaluate(self, wallet):
        return wallet.amount * 0.05


class two_percent:

    def evaluate(self, wallet):
        return wallet.amount * 0.02
