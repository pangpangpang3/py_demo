#!/usr/bin/env python
# -*- coding:utf-8 -*-

user_wage=0
shopping_dict = dict()

def output_shoppinglist():
    shopping_file = file("shopping_info.txt", "r")
    while True:
        shopping_item = shopping_file.readline()
        ##output the shopping list
        print(shopping_item)
        if len(shopping_item) != 0:
            shopping_list = shopping_item.split(" ")
            shopping_dict[shopping_list[0]] = int(shopping_list[1])
            continue
        else:
            break

def get_baseinfo():
    tmp_wage = input("Please input user wage:")
    global user_wage
    user_wage = tmp_wage
    print("user_wage:", user_wage)
    output_shoppinglist()

def check_afford():
    global shopping_info
    shopping_info = raw_input("Please input your the things your want to buy:")
    global user_wage
    if shopping_dict.has_key(shopping_info):
        if user_wage >= shopping_dict[shopping_info]:
            user_wage = user_wage - shopping_dict[shopping_info]
            print("You can afford it!, the rest money:%d" % user_wage )
            return True
        else:
            print("Sorry, you can't afford it now!")

            return False
    else:
        print("It's not in shopping list.")
        return True

def get_finally_wage():
    while True:
       if not check_afford():
           break

if __name__ == "__main__":
    get_baseinfo()
    get_finally_wage()


