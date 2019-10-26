# -*- coding: UTF-8 -*-


def evaluate_for_more_than_one_hundred_dollars(wallet):
    if wallet.amount >= 100:
        return wallet.amount * 0.1


def evaluate_for_more_than_three_stocks(wallet):
    if wallet.stocks >= 3:
        return wallet.amount * 0.05
