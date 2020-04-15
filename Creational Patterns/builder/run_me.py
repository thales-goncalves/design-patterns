# -*- coding: UTF-8 -*-

if __name__ == "__main__":

    from builder.builder import ComputerBuilder
    from builder.technical_leader import TechnicalLeader
    import pprint

    builder = ComputerBuilder()
    director = TechnicalLeader()
    director.builder = builder

    computer1 = director.createMasterGamingPC()
    computer2 = director.createLowLevelGamingPC()

    computers = [computer1, computer2]

    print('---------------------------------')
    for computer in computers:
        print(repr(computer))
        print('---------------------------------')
