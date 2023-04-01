'''
Simple Banking System
The project is to build a program that simulates a simple banking system. The program should allow users to create accounts,
 make deposits and withdrawals, check their balances, and transfer funds between accounts.
Operations that are to be allowed:
- create account: create a new account
- deposit: enter an amount into an account
- withdrawal: pull some amount from an account
- check balance: check all account details
- transfer: move amounts between accounts
- An account should have the following:
    - Name
    - Initial Balance
    - Account Number
    - Your code should handle user errors appropraitely.
You are allowed to use any desing you want. Check the best data types that you think fit for this project.
Make sure to document your code well and prepare for a code review.
'''
def chooses(users):
    print("Hi, customer\nchoose:\n1_ create accont\n2_ login system")
    choose = int(input("Enter the choose :"))
    if choose == 1:
        create_accont(users)
    elif choose == 2:
        login_accont(users)
    else:
        print("The choose not range")
def Logout(users):
    return chooses(users)

def chooses_type(users, username):
    print(f"Welcome, {username}!\nChoose:\n1_ Deposit \n2_ Withdrawal \n3_ Transfer \n4_ Check Balance \n5_ Logout")
    choose = int(input("Enter the choose :"))
    if choose == 1:
        deposit(users, username)
    elif choose == 2:
        withdrawal(users, username)
    elif choose == 3:
        Transfer(users, username)
    elif choose == 4:
        check_balance(users, username)
    elif choose == 5:
        Logout(users)
    else:
        print("The choose not range")


def deposit(users, username):
    deposit = float(input("Enter the deposit :"))
    deposit += users[username]['Initial_Balance']
    users[username] = {'Initial_Balance': deposit ,}
    return chooses_type(users, username)


def withdrawal(users, username):
    withdrawal = float(input("Enter the withdrawal :"))
    withdrawal -= users[username]['Initial_Balance']
    users[username] = {'Initial_Balance': withdrawal, }
    return chooses_type(users, username)


def Transfer(users, username):
    username_T = input("Enter the username_T :")
    for i in users:
        if username_T == i:
            print("Not username True")
            Transfer(users, username)
    transfer = float(input("Enter the transfer :"))
    transfere = transfer - users[username]['Initial_Balance']
    users[username] = {'Initial_Balance': transfere, }
    transferr = transfer + users[username_T]['Initial_Balance']
    users[username_T] = {'Initial_Balance': transferr, }
    return chooses_type(users, username)


def check_balance(users, username):
    Initial_Balance = users[username]['Initial_Balance']
    print(f"The Initial Balance for {username}: {Initial_Balance}")
    return chooses_type(users, username)


def create_accont(users):
    print("Hi, Thes Create Accont")
    username = input("Enter the username :")
    for i in users:
        if username == i:
            print("Enter Different username")
            create_accont(users)
    Name = input("Enter the Name :")
    Account_Number = int(input("Enter the Account Number :"))
    Initial_Balance = float(input("Enter the Initial Balance :"))
    password = input("Enter the password :")
    users[username] = {'Name': Name, 'Account_Number': Account_Number, 'Initial_Balance': Initial_Balance,
                       'password': password}
    return login_accont(users)


def login_accont(users):
    print("Hi, Thes Login Accont")
    username = input("Enter the username :")
    password = input("Enter the password :")
    if username in users and users[username]['password'] == password:
        # print("Welcome, " + username + "!")
        chooses_type(users, username)
    else:
        print("Error: Invalid username or password.")
        return login_accont(users)


if __name__ == '__main__':
    users = {'hussam': {
        'Name': 'hus',
        'Account_Number': 101,
        'Initial_Balance': 160.0,
        'password': '123',
    },
        'ahmed': {
            'Name': 'sam',
            'Account_Number': 102,
            'Initial_Balance': 50.0,
            'password': '123',
        },
        'mahmmod': {
            'Name': 'hu',
            'Account_Number': 103,
            'Initial_Balance': 100.0,
            'password': '123',
        },
    }
    chooses(users)


