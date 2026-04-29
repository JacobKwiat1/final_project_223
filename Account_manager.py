import json
import Account
class Account_manager:
    def __init__(self, file='users.txt'):
        self.file = file
        #empty dict first in case empty file
        self.accounts = {}

        with open(self.file, 'r') as f:
            self.accounts.update(json.load(f))
        #stick rawAccounts into dict as Account objects
        for account in self.accounts:
            self.accounts[account] = Account.load_data(self.account[account])

    
    def is_account_real(self, user):
        if user in self.account:
            return True
        return False
    
    def add_friend(self, friender, friendee):
        if not (friender in self.accounts and friendee in self.accounts):
            return False
        self.accounts[friender.get_username()].add_friend(friendee.get_username())

    def add_blocked(self, blocker, blockee):
        if not (blocker in self.accounts and blockee in self.accounts):
            return False
        self.accounts[blocker.get_username()].add_blocked(blockee.get_username())

    def save_data(self, file='users.txt'):
        for account in self.accounts:
            self.accounts[account] = self.accounts[account].prep_to_save()
        with open(file, 'w') as f:
            json.dump(self.accounts, f)
    
    def get_user(self, user):
        if user in self.accounts:
            return self.accounts[user]
        return False
    
    def create_account(self, username, password):
        if username in self.accounts:
            return False
        
        self.accounts[username] = Account.Account(username, password)