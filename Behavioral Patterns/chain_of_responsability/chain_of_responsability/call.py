# -*- coding: UTF-8 -*-
class Call:

    def __init__(self, complexity):
        self.__on_call = 0
        self.__answered_by = 'Machine'
        self.__complexity = complexity

    @property
    def on_call(self):
        return self.__on_call

    @property
    def complexity(self):
        return self.__complexity

    @property
    def answered_by(self):
        return self.__answered_by

    def add_minutes(self, minute):
        self.__on_call += minute

    def answered(self, service):
        self.__answered_by = service
