coffee_is_grinding = True

# def press_grind_beans():
#     global coffee_is_grinding
#     if coffee_is_grinding == True:
#         print("Stopping the grind")
#         coffee_is_grinding = False
#     elif coffee_is_grinding == False:
#         print("Grinding is about to begin")    
#         coffee_is_grinding = True

# coffee_is_grinding = False
# press_grind_beans()
# print(coffee_is_grinding)    



# Functions 
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