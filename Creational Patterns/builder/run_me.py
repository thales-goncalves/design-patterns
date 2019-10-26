# -*- coding: UTF-8 -*-

if __name__ == "__main__":

    from builder.builder import ComputerBuilder
    import pprint
    computer_builder = ComputerBuilder()
    computer1 = (computer_builder
                 .with_case('C300')
                 .with_motherboard('ASUS')
                 .with_cpu('INTEL')
                 .with_ram('16GB')
                 .with_hard_drive('1TB')
                 .with_power_supply('750W')
                 .build())

    computer2 = (computer_builder
                 .with_case('COSMUS II')
                 .with_motherboard('GIGABYTE')
                 .with_cpu('AMD')
                 .with_ram('32GB')
                 .with_hard_drive('2TB')
                 .with_power_supply('1000W')
                 .with_others_components('DVD Reader')
                 .build())

    computer3 = (computer_builder
                 .with_case('LAPTOP')
                 .with_motherboard('ASUS')
                 .with_cpu('AMD')
                 .with_ram('4GB')
                 .with_hard_drive('250GB')
                 .with_power_supply('420W')
                 .with_others_components('Backpack')
                 .build())

    computers = [computer1, computer2, computer3]

    print('---------------------------------')
    for computer in computers:
        print(repr(computer))
        print('---------------------------------')
