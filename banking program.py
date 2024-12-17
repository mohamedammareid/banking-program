import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_centered(text, width=30):
    print(text.center(width))

def show_balance(balance):
    clear_screen()
    print("\n💰" + "*" * 30 + "💰")
    print_centered("BALANCE", 30)
    print("*" * 30 + "💰\n")
    print(f"Your balance is: 💵 ${balance:.2f}")
    input("\nPress Enter to return to the menu...")

def deposit():
    clear_screen()
    print("\n💸" + "*" * 30 + "💸")
    print_centered("DEPOSIT", 30)
    print("*" * 30 + "💸\n")
    amount = float(input("Enter an amount to deposit 🤑: "))
    
    if amount <= 0:
        print("\n❌ That's not a valid amount ❌")
        input("\nPress Enter to return to the menu...")
        return 0
    else:
        return amount

def withdraw(balance):
    clear_screen()
    print("\n🏧" + "*" * 30 + "🏧")
    print_centered("WITHDRAW", 30)
    print("*" * 30 + "🏧\n")
    amount = float(input("Enter an amount to withdraw 💳: "))
    
    if amount > balance:
        print("\n❌ Insufficient funds ❌")
    elif amount <= 0:
        print("\n❌ Amount must be greater than 0 ❌")
        amount = 0
    else:
        return amount

    input("\nPress Enter to return to the menu...")
    return 0

def main():
    balance = 0.0
    is_running = True

    while is_running:
        clear_screen()
        print("\n🏦" + "*" * 30 + "🏦")
        print_centered("🏧 BANKING APP 🏧", 30)
        print("*" * 30 + "🏦\n")
        print("1️⃣. Show Balance 💰")
        print("2️⃣. Deposit 💵")
        print("3️⃣. Withdraw 💳")
        print("4️⃣. Exit 🚪")
        print("\n" + "*" * 30 + "\n")
        
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            clear_screen()
            print("\n👋" + "*" * 30 + "👋")
            print_centered("Thank you! Have a nice day! 😊", 30)
            print("*" * 30 + "👋\n")
            is_running = False
        else:
            print("\n❗ That is not a valid choice. Try again! ❗")
            input("\nPress Enter to return to the menu...")

if __name__ == '__main__':
    main()
