#!/usr/bin/env python

class person:
    def info(self, name, age):
        print("person's info name:%s, person's info age:%s"% (name, age))


P = person()
P.info("OldBoy", 35)

person().info("Stupid", 40)
