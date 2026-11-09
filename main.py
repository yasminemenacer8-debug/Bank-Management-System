from database import load_data, save_data 
accounts = load_data()

def create_account(accounts):
    print("===== CREATE ACCOUNT =====")
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")


    for acount in accounts:
        if acount["account_number"] == account_number:
            print("Account number already exists!")
            return
    name = input("Enter account holder name: ")
    try:
         balance = float(input("Enter initial balance: "))
         if balance < 0:
             print("Initial balance cannot be negative!")
             return
    except ValueError:
        print("Invalid input for initial balance!")
        return
    new_account = {
        "name": name,
        "account_number": account_number,
        "balance": balance
    }
    accounts.append(new_account)
    save_data(accounts)
    print("Account created successfully!")
    
def display_accounts(accounts):
    print("===== DISPLAY ACCOUNTS =====")
    if not accounts:
        print("No accounts found!")
        return
    for account in accounts:
        print(f"Name: {account['name']}, Account Number: {account['account_number']}, Balance: {account['balance']}")
        print()
def deposit(accounts):
    print("===Despoit===")
    account_number = input("Enter account number: ")
    
    for account in accounts:
        if account["account_number"] == account_number:
         try:
            
            print("Account found!",account["name"])
            amount = float(input("Enter deposit amount: "))
            if amount > 0:
                account["balance"] += amount
                save_data(accounts)
                print("Deposit successful! New balance:", account["balance"])
            else:
                print("Invalid deposit amount!\n")
         except ValueError:
            print("Invalid input!Please. enter a valid number.\n")
            return
    print("Account not found!")
         
def withdraw(accounts):         
        print("=== Withdraw===") 
        account_number = input("Enter account number: ")
        
        for account in accounts:
            if account["account_number"] == account_number:
             try:
                  
                  amount = float(input("Enter withdrawal amount: "))
                  if 0 < amount <= account["balance"]:
                    account["balance"] -= amount
                    print("Withdrawal successful! New balance:", account["balance"])
                  else:
                    print("Invalid withdrawal amount!")
                
             except ValueError:
                 print("invalid input! Please enter a valid number.\n")
                 return
        print("Account not found!")
def main():
     while True:
      print("===== BANK MANAGEMENT SYSTEM =====")
      print("1. Create Account")
      print("2. Display Accounts")
      print("3. Deposit")
      print("4. Withdraw")
      print("5. Exit")
      choice= input("Choose an option: ")
      if choice == "1":
        create_account()
      elif choice == "2":
        display_accounts()
      elif choice == "3":
         deposit()
      elif choice == "4":
        withdraw()
      elif choice == "5":
        print(" Exiting program.Good bye!")
        break
      else:
        print("Invalid option.")
if __name__ == "__main__":
 main()
    