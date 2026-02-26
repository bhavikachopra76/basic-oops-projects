import json
import string
import random
from pathlib import Path

class Bank:
    database = 'data.json'
    data = []
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("Database does not exist")
    except Exception as err:
        print(err)

    @staticmethod
    def __update():
        with open(Bank.database , 'w') as fs:
            json.dump(Bank.data , fs)

    @classmethod
    def __account_generate(cls):
        alpha = random.choices(string.ascii_letters, k = 3)
        num = random.choices(string.digits, k = 3)
        spchar = random.choices("!@#$%^&*" , k = 1)
        acc_no = alpha + num + spchar
        random.shuffle(acc_no)
        return "".join(acc_no)

    @staticmethod
    def create_account():
        info = {
            "name" : input("Enter your name: "),
            "age" : int(input("Enter your age: ")),
            "email" : input("Enter your email: "),
            "pin" : input("Enter your 4 number pin: "),
            "account_no." : Bank.__account_generate(),
            "balance" : 0
        }

        if info['age']<18 or len(str(info['pin'])) != 4:
            print("Sorry! You can not create your account")
        else:
            print("Account has been created successfully!")
            for i in info:
                print(f"{i}: {info[i]}")
            print("Please note down your account number")
            Bank.data.append(info)
            Bank.__update()

    @staticmethod
    def deposit_money():
        acc_number = input("Enter your account number: ").strip()
        pin = input("Enter your 4 number pin: ").strip()
        user_data = [x for x in Bank.data if x['account_no.']==acc_number and x['pin']==pin]
        if not user_data:
            print("Sorry! Account number doesn't exist")
        else:
            amount = int(input("Enter your deposit amount: "))
            if amount > 10000:
                print("Sorry! You cannot deposit more than 10000")
            elif amount < 0:
                print("Sorry! You cannot deposit less than 0")
            else:
                user_data[0]['balance'] += amount
                Bank.__update()
                print("Deposited successfully!")

    @staticmethod
    def withdraw_money():
        acc_number = input("Enter your account number: ").strip()
        pin = input("Enter your 4 number pin: ").strip()
        user_data = [x for x in Bank.data if x['account_no.'] == acc_number and x['pin'] == pin]
        if not user_data:
            print("Sorry! Account number doesn't exist")
        else:
            amount = int(input("Enter amount you want to withdraw: "))
            if user_data[0]['balance'] < amount:
                print("Sorry! Insufficient Balance")
            elif amount < 0:
                print("Sorry! You cannot deposit less than 0")
            else:
                user_data[0]['balance'] -= amount
                Bank.__update()
                print("Withdrew successfully!")

    @staticmethod
    def show_details():
        acc_number = input("Enter your account number: ").strip()
        pin = input("Enter your 4 number pin: ").strip()
        user_data = [x for x in Bank.data if x['account_no.'] == acc_number and x['pin'] == pin]
        print("Your details:")
        for i in user_data[0]:
            print(f"{i}: {user_data[0][i]}")
    @staticmethod
    def update_details():
        acc_number = input("Enter your account number: ").strip()
        pin = input("Enter your 4 number pin: ").strip()
        user_data = [x for x in Bank.data if x['account_no.'] == acc_number and x['pin'] == pin]
        if not user_data:
            print("Sorry! Account number doesn't exist")
        else:
            print("You cannot update age, account number, balance")
            print("Fill the details below or leave it empty if no change")
            new_data = {
                "name" : input("Enter your new name or press enter to skip: "),
                "email" : input("Enter your new email or press enter to skip: "),
                "pin" : input("Enter your new 4 number pin or press enter to skip: "),
            }

            if new_data['name']== "":
                new_data['name'] = user_data[0]['name']
            if new_data['email']== "":
                new_data['email'] = user_data[0]['email']
            if new_data['pin']== "":
                new_data['pin'] = user_data[0]['pin']
            new_data['account_no.'] = user_data[0]['account_no.']
            new_data['balance'] = user_data[0]['balance']
            new_data['age'] = user_data[0]['age']

            for i in new_data:
                if new_data[i] == user_data[0][i]:
                    continue
                else:
                    user_data[0][i] = new_data[i]

            Bank.__update()
            print("Updated successfully!")

    @staticmethod
    def delete_account():
        acc_number = input("Enter your account number: ").strip()
        pin = input("Enter your 4 number pin: ").strip()
        user_data = [x for x in Bank.data if x['account_no.'] == acc_number and x['pin'] == pin]
        if not user_data:
            print("Sorry! Account number doesn't exist")
        else:
            chk = input("Press y|n: ").lower()
            if chk == "n":
                print("Bypassing account")
            else:
                index = Bank.data.index(user_data[0])
                Bank.data.pop(index)
                print("Deleted successfully!")
                Bank.__update()

user = Bank()
print("Press 1 for Creating an account")
print("Press 2 for Depositing the money in the bank")
print("Press 3 for Withdrawing the money")
print("Press 4 for Details")
print("Press 5 for Updating the details")
print("Press 6 for Deleting your account")

check = int(input("Enter your choice: "))
if check == 1:
    user.create_account()
if check == 2:
    user.deposit_money()
if check == 3:
    user.withdraw_money()
if check == 4:
    user.show_details()
if check == 5:
    user.update_details()
if check == 6:
    user.delete_account()
