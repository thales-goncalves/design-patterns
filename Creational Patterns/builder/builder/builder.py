# -*- coding: UTF-8 -*-
from .computer import Computer


class ComputerBuilder:

    def __init__(self):
        self.__case = None
        self.__motherboard = None
        self.__cpu = None
        self.__ram = None
        self.__hard_drive = None
        self.__power_supply = None
        self.__others = None

    def with_case(self, case):
        self.__case = case
        return self

    def with_motherboard(self, motherboard):
        self.__motherboard = motherboard
        return self

    def with_cpu(self, cpu):
        self.__cpu = cpu
        return self

    def with_ram(self, ram):
        self.__ram = ram
        return self

    def with_hard_drive(self, hard_drive):
        self.__hard_drive = hard_drive
        return self

    def with_power_supply(self, power_supply):
        self.__power_supply = power_supply
        return self

    def with_others_components(self, others):
        self.__others = others
        return self

    def build(self):
        if self.__motherboard is None:
            raise Exception("Motherboard is mandatory")
        if self.__cpu is None:
            raise Exception("CPU is mandatory")
        if self.__ram is None:
            raise Exception("RAM is mandatory")
        if self.__hard_drive is None:
            raise Exception("HD is mandatory")
        if self.__power_supply is None:
            raise Exception("Power supply is mandatory")

        return Computer(
            case=self.__case,
            motherboard=self.__motherboard,
            cpu=self.__cpu,
            ram=self.__ram,
            hard_drive=self.__hard_drive,
            power_supply=self.__power_supply,
            others=self.__others
        )
