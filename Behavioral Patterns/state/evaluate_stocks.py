# -*- coding: UTF-8 -*-

from stock_exchange import twenty_percent, ten_percent, five_percent, two_percent


class evaluate_stocks:
    def evaluate(self, wallet, method):

        profit = method.evaluate(wallet)
        return profit


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 30))
    wallet.append_stock(Stock('Apple', 30))

    wallet.apply_extra_profit()
    print(wallet.amount)
    wallet.approve()
    wallet.apply_extra_profit()
    print(wallet.amount)
    wallet.terminate()
