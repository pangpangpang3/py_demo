#! /usr/bin/env python
# -*- coding: utf-8 -*-

id_dict = dict()
telephone_dict = dict()

username="penghui"
password="1976"

def get_info():
    read_file = open("info.txt", "r")
    while True:
        line = read_file.readline()
        if len(line)==0:
            break
        else:
            split_line = line.split(" ")
            id_dict[split_line[0]] = split_line[1]
            telephone_dict[split_line[0]] = split_line[2]

def check_password():
    num = 3
    while True:
        login_username = raw_input("please input your username:")
        login_password = raw_input("please input your password:")
        if login_username == username and login_password == password:
            return True
        else:
            print "wrong password!"
            num = num - 1
            if num == 0:
                print "wrong password for three times!"
            else:
                continue
            return False

def get_user_info():
    tmp_username = raw_input("please enter the username your need to check:")
    print id_dict[tmp_username]
    print telephone_dict[tmp_username]


if __name__ == "__main__":
    get_info()
    right_password = check_password()
    if right_password:
        get_user_info()
    else:
        print "Please reset you password!"
