The code is made for a banking system to create a personal account with a unique number to deposit, withdraw, check balance and transaction history.
To use the code, you have to provide a personal number of your account, your name and chose an operation you want to do, for example:
Personal number:"1111", Account holder: "Name", Deposit(amount of money you want to deposit), Withdraw(amount should be a number you have on your balance, otherwise, an error will occur),
Get balance(to check your balance), Transaction history(to get every type of transaction, its accomplished time and amount).

The code consists of two classes: Amount and Personal Account.
In the first class we create a transaction providing amount of money(self.amount), timestamp(datetime.now()), transaction type(self.transaction_type) and __str__ method to print out atributes. Its stores transactions made.

Personal account class has atributes to store self.account_number, self.account_holder, self.balance set to 0.0, self.transactions which is just an empty list to contain transaction history.
The methods are deposit(amount) to deposit money, withdraw(amount) to withdraw money, print_transaction_history() to store transactions in transaction list and print out history of transactions.
Also it has get_balance to check balance, get_account_number to check account number, get_account_holder to check name of an account holder. __str__ to return atributes, __add__ which is just a deposit method,
__sub__ same as withdraw method.<img width="653" alt="Снимок экрана 2025-02-12 в 13 05 02" src="https://github.com/user-attachments/assets/c1c4b0ff-9073-49df-aac4-0f0f8ab52a2e" />
