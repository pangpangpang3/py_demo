#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Person:
    def __init__(self, Name, Age, Sex):
        self.name = Name
        self.age = Age
        self.sex = Sex

    def talk(self, msg=0):
        self.msg = msg
        if self.msg != 0:
            print self.name, 'Saying:', self.msg

class person_info(Person):
    def __init__(self, Name, Age, Sex, nation, work):
        Person.__init__(self, Name, Age, Sex)
        self.country = nation
        self.job = work

    def tell(self, msg):
        print '''%s's person information:
            Name: %s
            Age: %s
            Sex: %s
            Nation: %s
            Work: %s
            '''%(self.name, self.name, self.age, self.sex, self.country, self.job)

pA = person_info("PP", 28, "f", 'CN', "walk")
pA.talk(2)
pA.tell(3)
