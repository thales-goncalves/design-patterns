# -*- coding: UTF-8 -*-
from .builder_interface import IBuilder
from .computer import Computer


class Technician(IBuilder):
    def __init__(self) -> None:
        self.reset()

    def computer(self) -> Computer:
        computer = self._computer
        self.reset()
        return computer

    def reset(self) -> None:
        self._computer = Computer()

    def with_case(self, case):
        self._computer.case = case
        return self

    def with_motherboard(self, motherboard):
        self._computer.motherboard = motherboard
        return self

    def with_cpu(self, cpu):
        self._computer.cpu = cpu
        return self

    def with_ram(self, ram):
        self._computer.ram = ram
        return self

    def with_hard_drive(self, hard_drive):
        self._computer.hard_drive = hard_drive
        return self

    def with_power_supply(self, power_supply):
        self._computer.power_supply = power_supply
        return self

    def with_others_components(self, others):
        self._computer.others = others
        return self

    def build(self):
        computer = self._computer
        self.reset()

        # if computer.motherboard is None:
        #     raise Exception("Motherboard is mandatory")
        # if computer.cpu is None:
        #     raise Exception("CPU is mandatory")
        # if computer.ram is None:
        #     raise Exception("RAM is mandatory")
        # if computer.hard_drive is None:
        #     raise Exception("HD is mandatory")
        # if computer.power_supply is None:
        #     raise Exception("Power supply is mandatory")

        return computer
