import random
import datetime

class DataBase:
    def __init__(self):
        self.accounts_credentials = {}

    def add_account_credentials(self, holder, password):
        self.accounts_credentials[holder] = password

    def check_credentials(self, holder, password):
        if self.accounts_credentials.get(holder) == password:
            return True
        return False

class BankAccount(DataBase):
    def create(self, type, balance, holder_name, password):
        self.__trans_history = []  # Transaction history list
        self.__password = password
        self.__holder_name = holder_name
        self.__type = type
        self.__balance = balance
        self.__acc_num = random.randint(0, 1000)  # Random account number
        super().add_account_credentials(self.__holder_name, self.__password)  # Save credentials
        print(f"Hi {holder_name},\nAccount number {self.__acc_num} of type {type} is created | Your balance = {balance}")

    def deposite(self, amount, holder_name, password):
        exist = super().check_credentials(holder_name, password)
        if exist:
            self.__balance += amount
            self.__trans_history.append(f"At time {datetime.datetime.now()} you deposited {amount}")
            print(f"At time {datetime.datetime.now()} you deposited {amount}")
        else:
            print("Wrong name or password")

    def withdraw(self, amount, holder_name, password):
        exist = super().check_credentials(holder_name, password)
        if exist:
            if amount <= self.__balance:
                self.__balance -= amount
                self.__trans_history.append(f"At time {datetime.datetime.now()} you withdrew {amount}")
                print(f"At time {datetime.datetime.now()} you withdrew {amount}, the current balance is {self.__balance}")
            else:
                print("Insufficient balance")
        else:
            print("Wrong name or password")

    def check_balance(self):
        return self.__balance

    def get_acc_type(self):
        return self.__type

    def get_acc_num(self):
        return self.__acc_num

    def get_holder_name(self):
        return self.__holder_name

    def keep_trans_history(self):
        for trans in self.__trans_history:
            print(trans)


def main():
    acc1 = BankAccount()
    acc1.create(type="Current", holder_name="Bishoy", password='123456', balance=3000)
    acc1.deposite(500, "Bishoy", '123456')
    acc1.withdraw(1000, "Bishoy", '123456')
    acc1.withdraw(1000, "Bishoy", '1234xs56')
    acc1.keep_trans_history()

    print(f"Account balance is: {acc1.check_balance()}")

main()
