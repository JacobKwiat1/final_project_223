import json
import Account
class Account_manager:
    def __init__(self, file='account_management.json'):
        self.file = file
        #empty dict first in case empty file
        self.accounts = {}
        try:
            with open(self.file, 'r') as f:
                self.accounts.update(json.load(f))
            #stick rawAccounts into dict as Account objects
            for account in self.accounts:
                self.accounts[account] = Account.load_data(self.accounts[account])
        except:
            with open(self.file, 'w') as f:
                pass

    def is_account_real(self, username):
        if username in self.account:
            return True
        return False
    
    def add_friend(self, friender, friendee):
        if not (friender in self.accounts and friendee in self.accounts):
            return False
        self.accounts[friender].add_friend(friendee)
        return True

    def remove_friend(self, friender, friendee):
        if not (friender in self.accounts and self.accounts[friender].is_friend(friendee)):
            return False
        self.accounts[friender].remove_friend(friendee)
        self.accounts[friendee].remove_friend(friender)
        return True

    def add_blocked(self, blocker, blockee):
        if not (blocker in self.accounts and blockee in self.accounts):
            return False
        self.accounts[blocker].add_blocked(blockee)
        return True

    def remove_blocked(self, blocker, blockee):
        if not (blocker in self.accounts and self.accounts[blocker].is_blocked(blockee)):
            return False
        self.accounts[blocker].remove_blocked(blockee)
        return True

    def save_data(self):
        for account in self.accounts:
            self.accounts[account] = self.accounts[account].prep_to_save()
        with open(self.file, 'w') as f:
            json.dump(self.accounts, f)
    
    def get_user(self, username):
        if username in self.accounts:
            return self.accounts[username]
        return False
    
    def create_account(self, username, password):
        if username in self.accounts:
            return False, "Username already in use"
        #todo: regex
        
        self.accounts[username] = Account.Account(username, password)
        return True

    def verify_login(self, username, password):
        if not username in self.accounts:
            return False
        return self.accounts[username].verify_login(password)
    
    def is_blocked(self, blocker, blockee):
        return self.accounts[blocker].is_blocked(blockee)
    
    def is_friend(self, friender, friendee):
        return self.accounts[friender].is_friend(friendee)
    
    def change_password(self, username, old_password, new_password):
        if self.accounts[username].verify_login(old_password):
            self.accounts[username].change_password(new_password)
            return True
        return False
    
    def send_request(self, requester, requestee):
        if requestee in self.accounts and not self.accounts[requestee].is_friend(requester):
            self.accounts[requestee].add_request(requester)
            return True
        return False
    
    def accept_request(self, requestee, requester):
        if not self.accounts[requestee].is_request(requester):
            return False
        self.accounts[requestee].accept_request(requester)
        self.accounts[requestee].add_friend(requester)
        return True
    
    def decline_request(self, requestee, requester):
        if not self.accounts[requestee].is_request(requester):
            return False
        self.accounts[requestee].decline_request(requester)
        return True
    
    def __repr__(self):
        out = ''
        for username in self.accounts:
            out += f'{self.accounts[username]}\n\n'
        return out