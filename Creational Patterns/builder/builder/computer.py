# -*- coding: UTF-8 -*-

import pprint


class Computer:
    def __init__(self):
        self.__case = None
        self.__motherboard = None
        self.__cpu = None
        self.__ram = None
        self.__hard_drive = None
        self.__power_supply = None
        self.__others = None

    @property
    def case(self):
        return self.__case

    @case.setter
    def case(self, case):
        self.__case = case

    @property
    def motherboard(self):
        return self.__motherboard

    @motherboard.setter
    def motherboard(self, motherboard):
        self.__motherboard = motherboard

    @property
    def cpu(self):
        return self.__cpu

    @cpu.setter
    def cpu(self, cpu):
        self.__cpu = cpu

    @property
    def ram(self):
        return self.__ram

    @ram.setter
    def ram(self, ram):
        self.__ram = ram

    @property
    def hard_drive(self):
        return self.__hard_drive

    @hard_drive.setter
    def hard_drive(self, hard_drive):
        self.__hard_drive = hard_drive

    @property
    def power_supply(self):
        return self.__power_supply

    @power_supply.setter
    def power_supply(self, power_supply):
        self.__power_supply = power_supply

    @property
    def others(self):
        return self.__others

    @others.setter
    def others(self, others):
        self.__others = others

    def __repr__(self):
        return '\n Case: {0},\n Motherboard: {1},\n CPU: {2},\n RAM: {3},\n HD: {4},\n Power Supply: {5},\n Other: {6}\n '.format(
            self.__case, self.__motherboard, self.__cpu, self.__ram,
            self.__hard_drive, self.__power_supply, self.__others)
