# -*- coding: UTF-8 -*-


class MachineAnswer:

    def __init__(self, next_evaluate):
        self.__next_evaluate = next_evaluate

    def answer(self, call):
        if call.complexity == 'easy':
            call.add_minutes(2)
            call.answered('Machine')
            return call
        else:
            return self.__next_evaluate.answer(call)


class CommomAnswer:

    def __init__(self, next_evaluate):
        self.__next_evaluate = next_evaluate

    def answer(self, call):
        call.add_minutes(2)
        if call.complexity == 'medium':
            call.add_minutes(5)
            call.answered('Human')
            return call
        else:
            return self.__next_evaluate.answer(call)


class TechnicalAnswer:

    def answer(self, call):
        call.add_minutes(5)
        call.add_minutes(8)
        call.answered('Technical Support')
        return call
