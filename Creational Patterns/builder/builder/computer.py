# -*- coding: UTF-8 -*-

import pprint


class Computer:

    def __init__(self, motherboard, cpu, ram, hard_drive, power_supply, case='', others=''):
        self.__case = case
        self.__motherboard = motherboard
        self.__cpu = cpu
        self.__ram = ram
        self.__hard_drive = hard_drive
        self.__power_supply = power_supply
        self.__others = others

    @property
    def case(self):
        return self.__case

    @property
    def motherboard(self):
        return self.__motherboard

    @property
    def cpu(self):
        return self.__cpu

    @property
    def ram(self):
        return self.__ram

    @property
    def hard_drive(self):
        return self.__hard_drive

    @property
    def power_supply(self):
        return self.__power_supply

    @property
    def others(self):
        return self.__others

    def __repr__(self):
        return '\n Case: {0},\n Motherboard: {1},\n CPU: {2},\n RAM: {3},\n HD: {4},\n Power Supply: {5},\n Other: {6}\n '.format(
            self.__case,
            self.__motherboard,
            self.__cpu,
            self.__ram,
            self.__hard_drive,
            self.__power_supply,
            self.__others
        )
