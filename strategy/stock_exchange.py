# -*- coding: UTF-8 -*-


def evaluate_for_more_than_ten_dollars(wallet):
    if wallet.amount > 10:
        return wallet.amount * 1.01


def evaluate_for_more_than_three_stocks(wallet):
    if wallet.stocks >= 3:
        return wallet.amount * 1.05
