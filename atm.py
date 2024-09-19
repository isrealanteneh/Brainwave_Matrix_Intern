import sys
from owner import account_owners

def main():
    print_menu()

# function to authenticate users PIN. 
# authenticate and return user
def auth():
    trial_count = 0 # the user allowed to enter PIN ONLY three time  
    try:
        user_pin = int(input("Please enter your PIN: ").strip())
        is_correct_pin = False # flag to check if the user found 
        while True:
            if trial_count == 2: # if user trial count is 2 user blocked
                print("Incorrect trail Your account is Blocked")
                break
            for user in account_owners:
                if user_pin == user.pin:
                    is_correct_pin = True
                    return user
            if is_correct_pin:
                break
            else:
                user_pin = int(input("Incorrect PIN, Please enter correct PIN: ").strip())
                trial_count += 1 # count after each trial untile 2 
    except ValueError:
        print("Please enter Numeric PIN!")
        return None
   
    

def atm_menu(user): # user is the succesfully logged in person 
    print("\n********************* Welcome",user.firstName,"*********************")
    print("Choose one of the following Options:")
    print("1. Deposite ")
    print("2. Withdraw ")
    print("3. Balance ")
    print("4. Exit ")
    try:
        option = int(input(": ").strip())    
    except ValueError:
        sys.exit("Sorry, you entered non numeric value ")
    if option == 1:
        deposite(user)
    elif option == 2:
        withdrawal(user)
    elif option == 3:
        balance(user)
    elif option == 4:
        print("Thank you, we are delighted to serve you")
        return True
    else:
        print("Invalid option ")


# function used to print menu items using while loop untile the user exit
def print_menu():
    logged_in_user = auth() 
    if logged_in_user is not None:
        exit = atm_menu(logged_in_user) # if the atm_menu() function return true while loop exit 
        while True:
            if exit:
                break
            exit = atm_menu(logged_in_user)
                          
    
def deposite(user):
    try:
        deposite_amount = float(input("Please enter the deposite amount: ").strip())
        user.set_balance(user.get_balance() + deposite_amount) # add the depoiste amount to the balance
        print(f"Dear customer your current balance is ${user.get_balance()}")
    except ValueError:
        print("sorry, you entered non-numeric value")
        return None

def withdrawal(user):
    try:
        withdrawal = float(input("Please enter the withdraw amount: ").strip())
        if user.get_balance() > withdrawal: # check if the balance is greater than withdraw amount
            user.set_balance(user.get_balance() - withdrawal)
            print(f"Dear Customer your current balance is ${user.get_balance()}")
        else:
            print("Insufficient balance to withdraw ")
    except ValueError:
        print("sorry, you entered non-numeric value")
        return None


def balance(user): 
    print(f"Dear Customer your balance is ${user.get_balance()}") # get the balance of logged in user



if __name__ == "__main__":
    main()




