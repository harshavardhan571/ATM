

from errors import *

balance = 7500

def deposit(gui_amount=None):
    global balance
    if gui_amount is None:
        dep = int(input("Enter deposit amount: "))
    else:
        dep = int(gui_amount)

    if dep < 100:
        raise Minimumdeposit
    else:
        balance += dep
        print(f"Your deposit amount of ₹{dep} is successful.")
        print(f"Total balance: ₹{balance}")

def withdraw(gui_amount=None):
    global balance
    if gui_amount is None:
        draw = int(input("Enter withdraw amount: "))
    else:
        draw = int(gui_amount)

    if draw > balance:
        raise lowbalance
    else:
        balance -= draw
        print(f"Withdraw amount of ₹{draw} is successful")
        print(f"Available balance: ₹{balance}")


def balanceenquiry(gui_mode=False):
    global balance
    if gui_mode:
        return f"Your balance is ₹{balance}"
    else:
        print(f"Your balance {balance}")

