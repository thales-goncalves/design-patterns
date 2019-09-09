# -*- coding: UTF-8 -*-

from stock_exchange import twenty_percent, ten_percent, five_percent, two_percent


class evaluate_stocks:
    def evaluate(self, wallet, exchange):

        profit = exchange.evaluate(wallet)
        return profit


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 30))
    wallet.append_stock(Stock('Apple', 30))

    exchange = evaluate_stocks()

    profit = exchange.evaluate(wallet, twenty_percent())
    print('Your current profit: US$', profit)
    profit = exchange.evaluate(wallet, ten_percent())
    print('Your current profit: US$', profit)
    profit = exchange.evaluate(wallet, five_percent())
    print('Your current profit: US$', profit)
    profit = exchange.evaluate(wallet, two_percent())
    print('Your current profit: US$', profit)

    print('\n')

    profit = exchange.evaluate(wallet, twenty_percent(two_percent()))
    print('Your current profit: US$', profit)
