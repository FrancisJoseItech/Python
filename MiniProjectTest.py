#iBank Banking
class ibank:
    def __init__(self):
        self.accounts={'arun11':{'name':'Arun','password':1231,'balance':1000.00},
                       'rishi11':{'name':'Rishi','password':2231,'balance':2000.00},
                       'varun11':{'name':'Varun','password':3321,'balance':3000.00}
                        }
#Login
    def login(self,userid,password):
        if userid in self.accounts and password==self.accounts[userid]['password']:
            print('Welcome to iBank. Happy Banking with us ')
            return True
        else:
            print('Account does not exist. Please create an account')
        bank.create_ibankac(user_id, user_password)


#Creating ibank account,when login fails
    def create_ibankac(self,userid,password):
        #creating new account if the userid does not exist
        if userid not in self.accounts:
            try:
                initial_deposit=float(input("Please make your initial deposit by entering the amount for your new account: "))
                name=input('Enter your name: ')
                self.accounts[userid]={'name':name,'password':password,'balance':initial_deposit}
                print(f'Your Account is created,{name} ')
                print(f'''Your account's userid is {userid}, password: {password} and your account balance is {initial_deposit}''')

            except ValueError:
                print('Enter a valid amount')
                bank.create_ibankac(user_id, user_password)

            return self.accounts[userid]
        else:
            print("userid already exists. Please try again.")
            print('Thank you')
            new_userid=input('Enter new userid: ')
            new_password=input('Enter your password: ')
            bank.create_ibankac(new_userid,new_password)



#Depositing
    def deposits(self,userid,amount):
        if userid in self.accounts:
            try:
                if amount<=0:
                    print('Please enter a valid amount')
                    return True
                self.accounts[userid]['balance']+=amount
                print(f'Your amount {amount} deposited successfully. New account balance is {self.accounts[userid]["balance"]}')
                print('Thank you for banking with iBank')
            except ValueError:
                print('Enter a valid amount to deposit')
        else:
            print('Please login, account not found')

#Withdrawal
    def withdrawal(self,userid,amount):
        if userid in self.accounts:
            try:
                if amount <=0:
                    print('Please enter a valid amount for withdrawal')
                    return True
                if self.accounts[userid]['balance']>=amount:
                    self.accounts[userid]['balance'] -=amount
                    print(f'You have withdrawn {amount} successfully. {self.accounts[userid]["name"]} your new balance is {self.accounts[userid]["balance"]}')
                    print('Thank you for banking with iBank')
                else:
                    print('Insufficient balance')
                    print('Thanks for banking with iBank')
            except:
                print('Please login, account not found')
#Display
    def display(self,userid):
        print(f'Welcome {self.accounts[userid]["name"]}. Your available balance is {self.accounts[userid]["balance"]}')
        print('Thanks for banking with iBank')

#creatingibank class
bank=ibank()

#Login or Create account
print('****** iBank Banking ******')
print('Please continue by login')

user_id=input('Enter your userid: ')
user_password=int(input('Enter your password: '))
bank.login(user_id,user_password)

#user input for methods
def startup_main():
    try:
        option=int(input('Press an option(1: Deposit, 2: Withdrawal, 3: Display Account, 4: Exit: '))
    except ValueError:
        print('Invalid option. Please enter a valid option')
        startup_main()
    if option==1:
        #Deposit
        try:
            deposit_amount=float(input('Please enter the amount to deposit: '))
        except ValueError:
            print('Invalid amount. Please enter a valid amount')
            deposit_amount = float(input('Please enter the amount to deposit'))
        except ValueError:
                print('Invalid amount. Please enter a valid amount')
                exit()
        bank.deposits(user_id,deposit_amount)
        startup_main()

    elif option==2:
        #withdrawal
        try:
            withdraw_amount=float(input('Enter the amount to withdraw: '))
        except ValueError:
            print('Invalid amount. Please enter a valid amount')
            exit()
        bank.withdrawal(user_id,withdraw_amount)
        startup_main()

    elif option==3:
        #Display Account details
        bank.display(user_id)
        startup_main()

    elif option==4:
        #Exit
        exit()

    else:
        print('Please enter a valid option. Thanks for visiting iBank')

startup_main()