import sys
import json

users = {}
def save():
    with open("data.json", "w") as f:
        json.dump(users, f)

with open("data.json", "r") as f:
    users = json.load(f)

pairs = {}
def save_balance():
    with open("cash.json", "w") as i:
        json.dump(pairs, i)
def open_balance():
    with open("cash.json", "r") as i:
        pairs = json.load(i)

with open("cash.json", "r") as i:
    pairs = json.load(i)


current_user = {}

def clear():
    users.clear()
    with open("data.json", "w") as f:
        json.dump(users, f)

def new_account():
    print("Please enter the following information.")
    while True:
        nun = input("Create Username: ")
        if 8 <= len(nun) <= 12 and nun not in users:
            c_nun = input("Please confirm Username: ")
            break
        elif nun in users:
                print("That username is taken.")
        else:
            print("Invalid input. Username must be between 8 and 12 characters.")
    while True:
        if c_nun == nun:
            print("Confirmed.")
            break
        else:
            print("Usernames do not match. Please try again.")
            c_nun = input("Please confirm Username: ")
    while True:
        npw = input("Please create a 4-digit pin: ")
        if npw.isnumeric() and len(npw) == 4:
            c_npw = float(input("Please confirm pin: "))
            break
        else:
            print("Invalid input. Please enter a 4-digit number.")
    while True:
        if c_npw == float(npw):
            print("Confirmed.")
            break
        else:
            print("Pins do not match. Please try again.")
            c_npw = float(input("Please confirm pin: "))

    first = input("First Name: ")
    last = input("Last Name: ")
    dob = input("Date of Birth (mm/dd/yyyy): ")
    if 2025 - int(dob[6:11]) < 18:
        print("You must be 18 or older to make an account.")
        sys.exit()

    pairs.update({str(c_nun): str(0)})
    users.update({str(c_nun): str(npw)})
    save()
    save_balance()
    print("Welcome to our bank\nPlease log in")
    login()

def login():
    name = input("Username: ")
    pw = input("Password: ")
    while True:
        if name in users and pw == users[name]:
            print("Authorization Accepted")
            current_user.update({name: pw})
            menu()
            break
        elif name in users and pw != users[name]:
            print("Incorrect Password. Try again.")
            pw = input("Password: ")
            if name in users and pw == users[name]:
                print("Authorization Accepted")
                current_user.update({name: pw})
                menu()
                break
            else:
                continue
        else:
            print("Username not in system")
            print("Would you like to:\n1. Create Account\n2. Try Again")
            choice = input("Select option (1 or 2): ")
            while True:
                if choice == "1":
                    new_account()
                    break
                if choice == "2":
                    name = input("Username: ")
                    pw = input("Password: ")
                    login()
                    break
                else:
                    print("Invalid Input. Please try again.")
                    choice = input("Select option (1 or 2): ")

def has_account():
    print("Welcome to our bank.")
    print("1. Login\n2. Create Account")
    choice = input("Select option (1 or 2): ")
    while True:
        if choice == "1":
            login()
            break
        if choice == "2":
            new_account()
            break
        else:
            print("Invalid Input. Please try again.")
            choice = input("Select option (1 or 2): ")

def menu():
    print("Bank Account")
    keys_view = current_user.keys()
    keys_list = list(keys_view)
    balance = pairs[keys_list[0]]
    print("Current Balance: $" + str(balance))
    print("1. Deposit\n2. Withdraw\n3. Exit")
    choice = input("Select option (1, 2, or 3): ")
    while True:
        if choice == "1":
            deposit()
            break
        if choice == "2":
            withdraw()
            break
        if choice == "3":
            keys_view = current_user.keys()
            keys_list = list(keys_view)
            name = keys_list[0]
            print("Have a nice day " + str(name) + ".")
            sys.exit()
        else:
            print("Invalid Input. Please try again.")
            choice = input("Select option (1, 2, or 3): ")

def deposit():
    open_balance()
    while True:
        try:
            depo = float(input("Please enter deposit amount: $"))
            break
        except ValueError:
            print("Must be a valid quantity.")
    keys_view = current_user.keys()
    keys_list = list(keys_view)
    balance = pairs[keys_list[0]]
    balance = float(balance) + depo
    print("Current Balance: $" + str(balance))

    pairs.update({keys_list[0]: str(balance)})
    save_balance()

    print("1. Return to Menu\n2. Additional Deposit")
    choice = input("Select option (1 or 2): ")
    while True:
        if choice == "1":
            menu()
            break
        if choice == "2":
            deposit()
            break
        else:
            print("Invalid Input. Please try again.")
            choice = input("Select option (1 or 2): ")

def withdraw():
    open_balance()
    while True:
        try:
            cash = float(input("Please enter withdrawal amount: $"))
            break
        except ValueError:
            print("Must be a valid quantity.")
    keys_view = current_user.keys()
    keys_list = list(keys_view)
    balance = pairs[keys_list[0]]
    balance = float(balance) - cash
    print("Current Balance: $" + str(balance))

    pairs.update({keys_list[0]: str(balance)})
    save_balance()

    print("1. Return to Menu\n2. Additional Withdrawal")
    choice = input("Select option (1 or 2): ")
    while True:
        if choice == "1":
            menu()
            break
        if choice == "2":
            withdraw()
            break
        else:
            print("Invalid Input. Please try again.")
            choice = input("Select option (1 or 2): ")
has_account()







