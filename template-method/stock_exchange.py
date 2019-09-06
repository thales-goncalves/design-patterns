# -*- coding: UTF-8 -*-


class twenty_percent:

    def evaluate(self, wallet):
        return wallet.amount * 1.2


class ten_percent:

    def evaluate(self, wallet):
        return wallet.amount * 1.1


class five_percent:

    def evaluate(self, wallet):
        return wallet.amount * 1.05


class two_percent:

    def evaluate(self, wallet):
        return wallet.amount * 1.02
