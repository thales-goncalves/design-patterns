# -*- coding: UTF-8 -*-


class evaluate_for_more_than_ten_thousand_dollars:

    def __init__(self, next_evaluate):
        self.__next_evaluate = next_evaluate

    def evaluate(self, wallet):
        if wallet.amount > 10000:
            return wallet.amount * 1.1
        else:
            return self.__next_evaluate.evaluate(wallet)


class evaluate_for_more_than_three_stocks:

    def __init__(self, next_evaluate):
        self.__next_evaluate = next_evaluate

    def evaluate(self, wallet):
        if wallet.stocks >= 3:
            return wallet.amount * 1.05
        else:
            return self.__next_evaluate.evaluate(wallet)


class evaluate_end:

    def evaluate(self, wallet):
        return 0
