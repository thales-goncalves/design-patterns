# -*- coding: UTF-8 -*-

from stock_exchange import twenty_percent, ten_percent, five_percent, two_percent


class evaluate_stocks:
    def evaluate(self, wallet, strategy):

        evaluate = strategy.evaluate(wallet)
        print(evaluate)


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 100))
    wallet.append_stock(Stock('Apple', 30))

    exchange = evaluate_stocks()

    print('20%:')
    exchange.evaluate(wallet, twenty_percent())
    print('10%:')
    exchange.evaluate(wallet, ten_percent())
    print('5%:')
    exchange.evaluate(wallet, five_percent())
    print('2%:')
    exchange.evaluate(wallet, two_percent())
