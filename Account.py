import hashlib
class Account:
    def __init__(self, username, password, friends=[], blocked=[], requests=[], new=True):
        self.username = username
        self.password = password
        if new:
            self.password = self.hash(password)
        self.friends = friends
        self.blocked = blocked
        self.requests = requests

    def __repr__(self):
        return f'username={self.username}\npassword={self.password}\nfriends={self.friends}\nblocked={self.blocked}'
    
    def hash(self, text):
        hashed_pass = text.encode()
        hashed_pass = hashlib.sha256(hashed_pass).hexdigest()
        return hashed_pass
    
    def prep_to_save(self):
        return {'username': self.username, 'password': self.password, 'friends':self.friends, 'blocked': self.blocked}
        
    def add_request(self, username):
        self.requests.append(username)

    def accept_request(self, request_name):
        self.friends.append(request_name)
        self.requests.remove(request_name)
    
    def decline_request(self, request_name):
        self.requests.remove(request_name)

    
    def add_friend(self, username):
        self.friends.append(username)

    def remove_friend(self, username):
        self.friends.remove(username)

    def add_blocked(self, username):
        self.blocked.append(username)

    def add_blocked(self, username):
        self.blocked.remove(username)

    def verify_login(self, password):
        if self.password == self.hash(password):
            return True
        return False
    
    def get_username(self):
        return self.username
    
    def is_friend(self, friend):
        if friend in self.friends:
            return True
        return False
    
    def is_blocked(self, blockee):
        if blockee in self.blocked:
            return True
        return False

    def get_blocked(self):
        return self.blocked
    
    def get_friends(self):
        return self.friends
    
    def get_requests(self):
        return self.requests
    
    def is_request(self, username):
        if username in self.requests:
            return True
        return False
    
    def change_password(self, password):
        self.password = password

#helper function as part of module but not class
def load_data(dict):
    return Account(dict['username'], dict['password'], dict['friends'], dict['blocked'], False)