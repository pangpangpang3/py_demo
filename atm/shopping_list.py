#!/usr/bin/env python
# -*- coding: utf-8 -*-

accountInfo = {'111':['123', 15000, 15000],
            '222':['456', 8000, 8000],
            '333':['789', 3000, 3000]
            }
global current_id
global shoppingItem
shoppingItem = list()
global moneyMount
moneyMount = list()
def initAccountInfo():
    accountInfo = {'111':['123','15000','15000'],
                   '222':['456','8000','8000'],
                   '333':['789','3000','3000']
                  }

def check_account():
    global current_id
    be_check_account = raw_input("Please input your account:")
    current_id = be_check_account
    print("current_id:", current_id)
    if accountInfo.has_key(be_check_account):
        print("The current account", current_id)
        if "belocked" in accountInfo[be_check_account]:
            print("Sorry your account be locked, please be unlocked!")
        else:
            enter_password_times = 3
            while True:
                be_check_password = (raw_input("Input the password:"))

                if be_check_password == accountInfo[be_check_account][0]:
                    # print("password is right!")
                    return True
                else:
                    enter_password_times = enter_password_times - 1
                    if enter_password_times == 0:
                        print("Sorry your account is be locked.")
                        accountInfo[be_check_account].append("belocked")
                        print("Your account be locked.")
                        return False
                        print("XXXXXXXXXXXXX")
                    else:
                        print("Sorry, wrong password!Please enter the password again:")
    else:
        print("Sorry, this account is not exist!")
        exit()

def shopping():
    global current_id
    shopping_thing = raw_input("Please input the things you want to buy:")
    shopping_price = int(raw_input("Please input the price:"))
    #the account balance can afford the shopping
    print ("print current id: ", accountInfo[currrent_id])
    if (shopping_price < accountInfo[current_id][2]):
        accountInfo[current_id][2] = accountInfo[current_id][2] - shopping_price
        shopping_dict.append(shopping_thing, shopping_price)
    #the credit balance can afford the shopping
    elif accountInfo[current_id][1] + accountInfo[current_id][2] > shopping_price:
        accountInfo[current_id][2] = accountInfo[current_id][2] - shopping_price
        shopping_dict.append(shopping_thing, shopping_price)
    else:
        print("Sorry you have already went over the top!")
        exit()

def query_account_balance():
    global current_id
    print("wort:", current_id)
    print("Your credit limit: %d\n" % accountInfo[current_id][1])
    print("Your account balance: %d\n" % accountInfo[current_id][2])

def transfer_account():
    global current_id
    global shoppingItem
    global moneyMount
    transfer_account = int(raw_input("Please enter the transfer account"))
    transfer_mount = int(raw_input("Please enter the amount transfer:"))
    #the account balance can afford the transfer
    if (accountInfo[current_id][2] > transfer_mount):
        accountInfo[current_id][2] = accountInfo[current_id][2] - transfer_mount
        shoppingItem.append("transfer")
        moneyMount.append(transfer_mount)
    # the credit balance can afford the shopping
    elif (accountInfo[current_id][2] + accountInfo[current_id][1] > transfer_mount):
        accountInfo[current_id][2] = accountInfo[current_id][2] - transfer_mount
        shoppingItem.append("transfer")
        moneyMount(transfer_mount)
    else:
        print("Sorry you have already went over the top!")

def withdrawals():
    global current_id
    global shoppingItem
    global moneyMount
    withdrawals = int(raw_input("Please enter withdrawals amount:"))

    #the account balance can afford the withdrawals
    if (accountInfo[current_id][2] > withdrawals):
        accountInfo[current_id][2] = accountInfo[current_id][2] - withdrawals
        shoppingItem.append("withdrawals")
        moneyMount.append(withdrawals)
        print("You have already withdrawals: %d" % withdrawals)
    elif (accountInfo[current_id][1] + accountInfo[current_id][2] > withdrawals):
        accountInfo[current_id][2] = accountInfo[current_id][2] - withdrawals
        shoppingItem.append("withdrawals")
        moneyMount.append(withdrawals)
        print("You have already withdrawals: %d" % withdrawals)
    else:
        print("Sorry you have already went over the top!")

def output_account():
    global current_id
    print("Date\t\tDescription\t\t\tCard number\t\t\tTransaction amount")
    for i in shoppingItem:
        print("\t\t\t%d\t\t\t%d" % shoppingItem[i], moneyMount[i])



if __name__ == "__main__":
    initAccountInfo()
    while True:
        if check_account():
            option = int(raw_input("#Welcome to XXX bank ATM ####\n\
                   #(1)Query balance\n\
                   #(2)Withdrawals\n\
                   #(3)Transfer_account\n\
                   #(4)Output account\n\
                   #(5)Other exit\n"))
            if option == 1:
                query_account_balance()
                continue
            elif option == 2:
                withdrawals()
                continue
            elif option == 3:
                output_account()
                continue
            elif option == 4:
                transfer_account()
                continue
            else:exit()
        else:break
