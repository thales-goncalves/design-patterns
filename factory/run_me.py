# -*- coding: UTF-8 -*-

if __name__ == "__main__":

    from factory.factory import CarFactory

    car_factory = CarFactory()
    cars = ['Audi', 'Chevrolet', 'Ford', 'Audi']

    print('---------------------------------')
    for car in cars:
        print(car_factory.createCar(car).model)
        print(car_factory.createCar(car).value)
        print('---------------------------------')
