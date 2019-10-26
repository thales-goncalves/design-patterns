# -*- coding: UTF-8 -*-

from stock_exchange import evaluate_for_more_than_one_hundred_dollars, evaluate_for_more_than_three_stocks


class evaluate_stocks:

    def evaluate(self, wallet, strategy):

        profit = strategy(wallet)
        return profit


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 30))
    wallet.append_stock(Stock('Apple', 30))

    exchange = evaluate_stocks()

    profit = exchange.evaluate(
        wallet, evaluate_for_more_than_one_hundred_dollars)
    print('Your current profit: US$', profit)
    profit = exchange.evaluate(wallet, evaluate_for_more_than_three_stocks)
    print('Your current profit: US$', profit)
