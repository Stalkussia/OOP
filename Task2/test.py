from personalaccount import PersonalAccount

if __name__ == '__main__':
    #Case 1: normal functioning
    test = PersonalAccount(11111,'Aiman')
    test.deposit(2000)
    test.withdraw(135)
    print(test.balance)
    test.print_transaction_history()

    #Case 2: not enough money on balance
    test1 = PersonalAccount(11112,"Zaire")
    test1.deposit(1000)
    test1.withdraw(1999)
    print(test1.balance)
    test1.print_transaction_history()

    #Case 3: Inappropriate deposit amount
    test2 = PersonalAccount(11113,"Pau")
    test2.deposit(-291)
    print(test2.balance)
    test2.print_transaction_history()