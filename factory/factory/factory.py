# -*- coding: utf-8 -*-
from factory.car import Car, Audi, Ford, Chevrolet


class CarFactory:
    def createCar(self, model):
        car_class = model.capitalize()
        return globals()[car_class]()
