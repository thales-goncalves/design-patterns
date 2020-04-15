from abc import ABC, abstractproperty, abstractmethod


class IBuilder(ABC):
    @abstractproperty
    def computer(self) -> None:
        pass

    @abstractmethod
    def with_case(self, case):
        pass

    @abstractmethod
    def with_motherboard(self, motherboard):
        pass

    @abstractmethod
    def with_cpu(self, cpu):
        pass

    @abstractmethod
    def with_ram(self, ram):
        pass

    @abstractmethod
    def with_hard_drive(self, hard_drive):
        pass

    @abstractmethod
    def with_power_supply(self, power_supply):
        pass

    @abstractmethod
    def build(self):
        pass