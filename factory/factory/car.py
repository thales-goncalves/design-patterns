# -*- coding: UTF-8 -*-


class Car:

    model = ''
    brand = ''
    value = ''

    def model(self):
        return self.model

    def value(self):
        return self.value


class Audi(Car):
    model = 'A3'
    value = '$ 15,000'


class Ford(Car):
    model = 'F250'
    value = '$ 13,000'


class Chevrolet(Car):
    model = 'Cruze'
    value = '$ 7,000'
