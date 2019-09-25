# -*- coding: UTF-8 -*-
from observer.observer import to_father, to_mother, to_hospital

class Student:

    def __init__(self, name, father, mother, hospital, description='', observers=[]):
        self.__name = name
        if len(description) > 20:
            raise Exception("Description cannot have more than 20 characters!")
        self.__description = description
        self.__father = father
        self.__mother = mother
        self.__hospital = hospital

        for observer in observers:
            observer(self)

    @property
    def name(self):
        return self.__name

    @property
    def father(self):
        return self.__father

    @property
    def mother(self):
        return self.__mother

    @property
    def description(self):
        return self.__description

    @property
    def hospital(self):
        return self.__hospital
