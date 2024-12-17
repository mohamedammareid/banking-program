
# Banking App

This is a console-based banking application that allows users to check their balance, deposit money, and withdraw money. The app uses simple input and output to simulate basic banking functionality with a user-friendly interface.

## Features:
- **Show Balance**: Displays the current balance.
- **Deposit**: Allows users to deposit a specified amount into their account.
- **Withdraw**: Allows users to withdraw a specified amount, provided they have sufficient funds.
- **Exit**: Closes the application.

## Usage:
1. The program starts with a main menu offering the following options:
   - **Show Balance**: View your current balance.
   - **Deposit**: Deposit a specified amount into your account.
   - **Withdraw**: Withdraw a specified amount (must be less than or equal to your balance).
   - **Exit**: Exit the app.
2. The program validates user inputs, ensuring that deposit and withdrawal amounts are valid.
3. The screen is cleared after each operation for a clean interface.

## Example Interaction:

```
🏦******************************🏦
           🏧 BANKING APP 🏧
******************************🏦

1️⃣. Show Balance 💰
2️⃣. Deposit 💵
3️⃣. Withdraw 💳
4️⃣. Exit 🚪

******************************

Enter your choice (1-4): 2

💸******************************💸
              DEPOSIT
******************************💸

Enter an amount to deposit 🤑: 50

Your balance is: 💵 $50.00
Press Enter to return to the menu...

```

## Functions:
1. **clear_screen()**: Clears the console screen for better readability.
2. **print_centered(text, width=30)**: Prints the provided text centered on the screen.
3. **show_balance(balance)**: Displays the user's current balance.
4. **deposit()**: Prompts the user to enter a deposit amount and returns it.
5. **withdraw(balance)**: Prompts the user to enter a withdrawal amount and returns it if valid.
6. **main()**: Main loop where users can interact with the app.

## Requirements:
- Python 3.x

## How It Works:
1. The app starts by showing a menu with four options: Show Balance, Deposit, Withdraw, and Exit.
2. The user can select an option by entering the corresponding number.
3. The app validates the inputs for deposit and withdrawal amounts.
4. The program ensures that the balance is updated correctly based on the user's actions.
5. The app continues running until the user chooses to exit.

---
