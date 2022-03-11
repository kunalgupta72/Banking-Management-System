import os
import pickle
import pathlib

# Account class
class Account:
    acc_number = 0
    holder_name = ''
    deposit = 0
    type = ''

    # here we creating new Account
    def createAccount(self):
        self.acc_number = int(input('Account number : '))
        self.holder_name = input('Holder Name : ')
        self.deposit = int(input('Deposit amount (>=500) : '))
        self.type = input('Account type : ')
        print('Account created......')

# end of account class

# 1 for creating new account
def newAccount():
    account = Account()
    account.createAccount()
    writeAccount(account)

# 4 Balance enquirey
def accountinfo(num):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        loadFile = pickle.load(openFile)
        openFile.close()

        for acc in loadFile:
            if (acc.acc_number == num):
                print('------------------------------------')
                print('Account Holder : {}'.format(acc.holder_name))
                print('Your account balance : {}'.format(acc.deposit))
                print('------------------------------------')
        else:
            print('No data for this account number😥')

# 2,3 deposit and withdrawl amount
def depositWithdrawlAmount(num, target):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        dataList = pickle.load(openFile)
        openFile.close()
        os.remove('account.data')
        found = False
        for holderList in dataList:
            if holderList.acc_number == num:
                found = True
                if target == 'd':
                    print("hey {}".format(holderList.holder_name))
                    depositAmount = int(input('Deposit Amount : '))
                    holderList.deposit += depositAmount
                    print('deposit successfully🙋')
                elif target == 'w':
                    print("hey {}".format(holderList.holder_name))
                    withdrawlAmount = int(input('withdrawl amount : '))
                    if withdrawlAmount > holderList.deposit:
                        print("You can't withdrawl this amount.")
                        print("Your currnet balance is {} only".format(holderList.deposit))
                        break
                    elif(withdrawlAmount <= holderList.deposit):
                        holderList.deposit -= withdrawlAmount
                        print('Your current amount : ', holderList.deposit)
        if not found:
            print('Your account is not exist😥')
    else:
        print('No data found....')
    outFile = open('newAccount.data', "wb")
    pickle.dump(dataList, outFile)
    outFile.close()
    os.rename("newAccount.data", "account.data")

# 5 Account List
def accountList():
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        accountList = pickle.load(openFile)
        openFile.close()
        if accountList == []:
            print('No data...')

        print('-----------Account List------------')
        for accList in accountList:
            print('------------------------------------')
            print('Account Number : {}'.format(accList.acc_number))
            print('Holder Name : {}'.format(accList.holder_name))
            print('Net Balance : {}'.format(accList.deposit))
            print('Account Type : {}'.format(accList.type))
            print('-------------------------------------')
    else:
        print('No data...')

# 6 Close Account
def closeAccount(num):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data',"rb")
        accountList = pickle.load(openFile)
        openFile.close()
        os.remove('account.data')
        newList = []

        for accList in accountList:
            if accList.acc_number !=num:
                newList.append(accList)
            else:
                print('Your account is deleted..')
                break
    else:
        print('You are not our customer...')
    outFile = open('newAccount.data',"wb")
    pickle.dump(newList,outFile)
    outFile.close()
    os.rename("newAccount.data","account.data")   

# basically this function is for creating text file(database)
def writeAccount(account):
    file = pathlib.Path('account.data')

    if file.exists():
        openFile = open('account.data', "rb")
        oldList = pickle.load(openFile)
        oldList.append(account)
        openFile.close()
        os.remove('account.data')
    else:
        oldList = [account]
    openFile = open('newAccount.data', "wb")
    pickle.dump(oldList, openFile)
    openFile.close()
    os.rename('newAccount.data', 'account.data')

# starting of the code
def into():
    print('********Welcome*********')
    print('****Bank of Horseman****')
    print()
into()

ch = ''
num = 0
while(ch != '0'):
    print('0 : Exit')
    print('1 : New Account')
    print('2 : Deposit')
    print('3 : Withdrawl')
    print('4 : Balance Enquirey')
    print('5 : All Account List')
    print('6 : Close Account')

    print('Choose option above....')
    ch = input()

    if (ch == '1'):
        newAccount()
    elif (ch == '2'):
        num = int(input('enter account number : '))
        depositWithdrawlAmount(num, 'd')
    elif(ch == '3'):
        num = int(input('enter account number : '))
        depositWithdrawlAmount(num, 'w')
    elif(ch == '4'):
        num = int(input('enter account number : '))
        accountinfo(num)
    elif(ch == '5'):
        accountList()
    elif (ch == '6'):
        num = int(input('enter the account number : '))
        closeAccount(num)