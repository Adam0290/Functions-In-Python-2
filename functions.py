balance = 1000

def withdaw_funds(amount, account_number):
    global balance
    print(f"you have requested {amount} from account {account_number}")
    if balance > amount: #colon is like a then
        balance = balance - amount
        print("Cash is in its on its way, you new balance is ",  + balance)
    else:
        print("You have insufficient funds")

withdaw_funds(100, 1231123)
