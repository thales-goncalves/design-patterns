from .builder import ComputerBuilder
from .builder_interface import IBuilder


class TechnicalLeader:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> IBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: IBuilder) -> None:
        self._builder = builder

    def createLowLevelGamingPC(self) -> None:
        return self.builder.with_case('C300').with_motherboard(
            'ASUS').with_cpu('INTEL').with_ram('16GB').with_hard_drive(
                '1TB').with_power_supply('750W').with_others_components(
                    'Backpack').build()

    def createMasterGamingPC(self) -> None:
        return self.builder.with_case('COSMUS II').with_motherboard(
            'GIGABYTE').with_cpu('AMD').with_ram('32GB').with_hard_drive(
                '2TB').with_power_supply('1000W').with_others_components(
                    'DVD Reader').build()
