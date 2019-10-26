# -*- coding: UTF-8 -*-
from stock_exchange import evaluate_for_more_than_ten_thousand_dollars, evaluate_for_more_than_three_stocks, evaluate_end


class evaluate_stocks:

    def evaluate(self, wallet):

        profit = evaluate_for_more_than_ten_thousand_dollars(
            evaluate_for_more_than_three_stocks(
                evaluate_end()
            )
        ).evaluate(wallet)
        return profit


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 9))
    wallet.append_stock(Stock('Apple', 50))

    exchange = evaluate_stocks()

    profit = exchange.evaluate(wallet)
    print('Your current profit: US$', profit)

    wallet.append_stock(Stock('Samsung', 1))

    profit = exchange.evaluate(wallet)
    print('Your current profit: US$', profit)
