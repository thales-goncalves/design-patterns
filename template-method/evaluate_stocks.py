# -*- coding: UTF-8 -*-
from stock_exchange import evaluate_for_more_than_ten_thousand_dollars, evaluate_for_more_than_three_stocks, evaluate_end


class evaluate_stocks:

    def evaluate(self, wallet):

        amount = evaluate_for_more_than_ten_thousand_dollars(
            evaluate_for_more_than_three_stocks(
                evaluate_end()
            )
        ).evaluate(wallet)
        return amount


if __name__ == '__main__':

    from stock import Stock, Wallet

    wallet = Wallet()
    wallet.append_stock(Stock('Microsoft', 40))
    wallet.append_stock(Stock('Google', 10))
    wallet.append_stock(Stock('Apple', 50))

    exchange = evaluate_stocks()

    evaluateStocks = exchange.evaluate(wallet)

    print(evaluateStocks)
