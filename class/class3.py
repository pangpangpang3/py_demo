#!/usr/bin/env python

class Student:
    def __init__(self, nationality):
        self.country_name = nationality

    def info(self, name, age):
        print("The student are from %s, her/his name is %s, her/his age is %s" % (self.country_name, name, age))


studentA = Student("CN")
studentA.info("Tom", 25)
