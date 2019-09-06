# -*- coding: UTF-8 -*-

from stock_exchange import evaluate_for_more_than_ten_dollars, evaluate_for_more_than_three_stocks


class evaluate_stocks:

    def evaluate(self, wallet, strategy):

        evaluate = strategy(wallet)

        print(evaluate)


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 10))
    wallet.append_stock(Stock('Apple', 50))

    exchange = evaluate_stocks()

    exchange.evaluate(wallet, evaluate_for_more_than_ten_dollars)
    exchange.evaluate(wallet, evaluate_for_more_than_three_stocks)
