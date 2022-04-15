user_1_account = {
    'name' : 'Vincent Vega',
    'accountNumber':'4579867',
    'balance': 3000,
    'additionalAcc': 2000
}

user_2_account = {
    'name' : 'Jules Winnfield',
    'accountNumber':'1456743',
    'balance': 2000,
    'additionalAcc': 1000
}

def withdrawMoney(account, amount):
    print(f"Hello {account['name']}!")
    
    if (account['balance'] >= amount):
        account['balance'] -= amount
        print('You can take your money.')
        balanceInquiry(account)
    
    else:
        summation = account['balance'] + account['additionalAcc']
        
        if (summation >= amount):
            additionalAccUsage = input('Do you want to use additional account?(y/n)')
            
            if additionalAccUsage == 'y':
                
                additionalAccUsageAmount = amount - account['balance']
                account['balance'] = 0
                account['additionalAcc'] -= additionalAccUsageAmount
                print('You can take your money.')
                balanceInquiry(account)
            
            else:
                print(f"You have ${amount} in your {account['accountNumber']} account.")
        else:
            print('Insufficient funds.')

def balanceInquiry(account):
    print(f"You have ${account['balance']} in your {account['accountNumber']} account.")
    print(f"Your limit of additional account is : ${account['additionalAcc']}.")
        
                
            
    
withdrawMoney(user_1_account, 3000)
print("********************************************")
withdrawMoney(user_1_account, 2000)
